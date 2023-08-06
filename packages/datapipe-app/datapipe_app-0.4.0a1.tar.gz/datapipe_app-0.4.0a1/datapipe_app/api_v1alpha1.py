from typing import Any, Dict, List, Literal, Optional

import pandas as pd
from datapipe.compute import (
    Catalog,
    ComputeStep,
    DataStore,
    Pipeline,
    run_steps,
    run_steps_changelist,
)
from datapipe.store.database import TableStoreDB
from datapipe.types import ChangeList
from fastapi import BackgroundTasks, FastAPI, Query, Response
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from pydantic import BaseModel, Field
from sqlalchemy.sql.expression import select, text
from sqlalchemy.sql.functions import count


class PipelineStepResponse(BaseModel):
    id_: str = Field(alias="id")
    type_: str = Field(alias="type")
    name: str
    inputs: List[str]
    outputs: List[str]


class TableResponse(BaseModel):
    name: str

    indexes: List[str]

    size: int
    store_class: str


class GraphResponse(BaseModel):
    catalog: Dict[str, TableResponse]
    pipeline: List[PipelineStepResponse]


class UpdateDataRequest(BaseModel):
    table_name: str
    upsert: Optional[List[Dict]] = None
    enable_changelist: bool = True
    # delete: List[Dict] = None


class UpdateDataResponse(BaseModel):
    result: str


class GetDataRequest(BaseModel):
    table: str
    filters: Dict[str, Any] = {}
    page: int = 0
    page_size: int = 20
    order_by: Optional[str] = None
    order: Literal["asc", "desc"] = "asc"


class GetDataResponse(BaseModel):
    page: int
    page_size: int
    total: int
    data: List[Dict]


def update_data(
    ds: DataStore,
    catalog: Catalog,
    steps: List[ComputeStep],
    req: UpdateDataRequest,
) -> UpdateDataResponse:
    dt = catalog.get_datatable(ds, req.table_name)

    cl = ChangeList()

    if req.upsert is not None and len(req.upsert) > 0:
        idx = dt.store_chunk(pd.DataFrame.from_records(req.upsert))

        cl.append(dt.name, idx)

    # if req.delete is not None and len(req.delete) > 0:
    #     idx = dt.delete_by_idx(
    #         pd.DataFrame.from_records(req.delete)
    #     )

    #     cl.append(dt.name, idx)
    if req.enable_changelist:
        run_steps_changelist(ds, steps, cl)

    return UpdateDataResponse(result="ok")


def get_data_get(
    ds: DataStore,
    catalog: Catalog,
    table: str,
    page: int = 0,
    page_size: int = 20,
) -> GetDataResponse:
    dt = catalog.get_datatable(ds, table)

    meta_schema = dt.meta_table.sql_schema
    meta_tbl = dt.meta_table.sql_table

    sql = select(*meta_schema)
    sql = sql.where(meta_tbl.c.delete_ts.is_(None))
    sql = sql.offset(page * page_size).limit(page_size)

    meta_df = pd.read_sql_query(
        sql,
        con=ds.meta_dbconn.con,
    )

    if not meta_df.empty:
        data_df = dt.get_data(meta_df)
    else:
        data_df = pd.DataFrame()

    return GetDataResponse(
        page=page,
        page_size=page_size,
        total=len(meta_df),
        data=data_df.fillna("").to_dict(orient="records"),
    )


def get_data_post(
    ds: DataStore, catalog: Catalog, req: GetDataRequest
) -> GetDataResponse:
    dt = catalog.get_datatable(ds, req.table)

    assert isinstance(dt.table_store, TableStoreDB)

    sql_schema = dt.table_store.data_sql_schema
    sql_table = dt.table_store.data_table

    sql = select(*sql_schema).select_from(sql_table)
    # Data table has no delete_ts
    # sql = sql.where(sql_table.c.delete_ts.is_(None))
    if req.order_by:
        sql = sql.where(text(f"{req.order_by} is not null"))
        sql = sql.order_by(text(f"{req.order_by} {req.order}"))
    sql = sql.offset(req.page * req.page_size).limit(req.page_size)

    for col, val in req.filters.items():
        sql = sql.where(sql_table.c[col] == val)

    sql_count = select(count()).select_from(sql_table)
    for col, val in req.filters.items():
        sql_count = sql_count.where(sql_table.c[col] == val)

    meta_df = pd.read_sql_query(
        sql,
        con=ds.meta_dbconn.con,
    )

    if not meta_df.empty:
        data_df = dt.get_data(meta_df)
        if req.order_by is not None:
            ascending = req.order == "asc"
            data_df.sort_values(by=req.order_by, ascending=ascending, inplace=True)
    else:
        data_df = pd.DataFrame()

    return GetDataResponse(
        page=req.page,
        page_size=req.page_size,
        total=dt.table_store.dbconn.con.execute(sql_count).fetchone()[0],
        data=data_df.fillna("").to_dict(orient="records"),
    )


def DatpipeAPIv1(
    ds: DataStore, catalog: Catalog, pipeline: Pipeline, steps: List[ComputeStep]
) -> FastAPI:
    app = FastAPI()

    @app.get("/graph", response_model=GraphResponse)
    def get_graph() -> GraphResponse:
        def table_response(table_name):
            tbl = catalog.get_datatable(ds, table_name)

            return TableResponse(
                name=tbl.name,
                indexes=tbl.primary_keys,
                size=tbl.get_size(),
                store_class=tbl.table_store.__class__.__name__,
            )

        def pipeline_step_response(step):
            inputs = [i.name for i in step.input_dts]
            outputs = [i.name for i in step.output_dts]
            inputs_join = ",".join(inputs)
            outputs_join = ",".join(outputs)
            id_ = f"{step.name}({inputs_join})->({outputs_join})"

            return PipelineStepResponse(
                id=id_,
                type="transform",
                name=step.get_name(),
                inputs=inputs,
                outputs=outputs,
            )

        return GraphResponse(
            catalog={
                table_name: table_response(table_name)
                for table_name in catalog.catalog.keys()
            },
            pipeline=[pipeline_step_response(step) for step in steps],
        )

    @app.post("/update-data", response_model=UpdateDataResponse)
    def update_data_api(req: UpdateDataRequest) -> UpdateDataResponse:
        return update_data(ds, catalog, steps, req)

    # /table/<table_name>?page=1&id=111&another_filter=value&sort=<+|->column_name
    @app.get("/get-data", response_model=GetDataResponse)
    def get_data_get_api(
        table: str,
        page: int = 0,
        page_size: int = 20,
    ) -> GetDataResponse:
        return get_data_get(ds, catalog, table, page, page_size)

    @app.post("/get-data", response_model=GetDataResponse)
    def get_data_post_api(req: GetDataRequest) -> GetDataResponse:
        return get_data_post(ds, catalog, req)

    class FocusFilter(BaseModel):
        table_name: str
        items_idx: List[Dict]

    class GetDataWithFocusRequest(BaseModel):
        table_name: str

        page: int = 0
        page_size: int = 20

        focus: Optional[FocusFilter] = None

    @app.post("/get-data-with-focus", response_model=GetDataResponse)
    def get_data_with_focus(req: GetDataWithFocusRequest) -> GetDataResponse:
        dt = catalog.get_datatable(ds, req.table_name)

        if req.focus is not None:
            idx = pd.DataFrame.from_records(
                [
                    {k: v for k, v in item.items() if k in dt.primary_keys}
                    for item in req.focus.items_idx
                ]
            )
        else:
            idx = None

        existing_idx = dt.meta_table.get_existing_idx(idx=idx)

        return GetDataResponse(
            page=req.page,
            page_size=req.page_size,
            total=len(existing_idx),
            data=dt.get_data(
                existing_idx.iloc[
                    req.page * req.page_size : (req.page + 1) * req.page_size  # noqa: E203
                ]
            ).to_dict(orient="records"),
        )

    class GetDataByIdxRequest(BaseModel):
        table_name: str
        idx: List[Dict]

    @app.post("/get-data-by-idx")
    def get_data_by_idx(req: GetDataByIdxRequest):
        dt = catalog.get_datatable(ds, req.table_name)

        res = dt.get_data(idx=pd.DataFrame.from_records(req.idx))

        return res.to_dict(orient="records")

    @app.post("/run")
    def run():
        run_steps(ds=ds, steps=steps)

    # TODO refactor out to component based extension system
    # TODO automatic setup of webhook on project creation
    @app.post("/labelstudio-webhook")
    def labelstudio_webhook(
        request: Dict,
        background_tasks: BackgroundTasks,
        table_name: str = Query(..., title="Input table name"),
        data_field: List = Query(..., title="Fields to get from data"),
        background: bool = Query(False, title="Run as Background Task (default = False)")
    ) -> None:

        upsert = [
            {
                **{
                    k: v
                    for k, v in request["task"]["data"].items()
                    if k in data_field
                },
                "annotations": [request["annotation"]],
            }
        ]

        dt = catalog.get_datatable(ds, table_name)

        cl = ChangeList()

        if len(upsert) > 0:
            idx = dt.store_chunk(pd.DataFrame.from_records(upsert))

            cl.append(dt.name, idx)

        if background:
            background_tasks.add_task(run_steps_changelist, ds=ds, steps=steps, changelist=cl)
        else:
            run_steps_changelist(ds=ds, steps=steps, changelist=cl)

    @app.get("/get-file")
    def get_file(filepath: str):
        import mimetypes

        import fsspec

        with fsspec.open(filepath) as f:
            mime = mimetypes.guess_type(filepath)
            assert mime[0] is not None
            return Response(content=f.read(), media_type=mime[0])

    FastAPIInstrumentor.instrument_app(app, excluded_urls="docs")

    return app
