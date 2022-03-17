from fastapi import FastAPI

from api.endpoints.routes.catalog_api import router
from api.core.config import settings as s


middleware = []


def get_catalogapp() -> FastAPI:
    application = FastAPI(
        title="Catalog",
        description="Catalog of Schemas, Issuers and Operations",
        debug=s.DEBUG,
        middleware=middleware,
    )
    # mount other endpoints, these will be secured by the above token endpoint
    application.include_router(
        router,
        prefix=s.API_V1_STR,
        dependencies=[],
        tags=["catalog"],
    )
    return application
