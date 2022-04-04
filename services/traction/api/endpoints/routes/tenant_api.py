from fastapi import APIRouter

from api.endpoints.routes import connections, credentials, tenant_admin
from api.endpoints.routes.holder import credentials as new_credentials

tenant_router = APIRouter()
tenant_router.include_router(
    connections.router, prefix="/connections", tags=["connections"]
)
tenant_router.include_router(
    credentials.router, prefix="/credentials", tags=["credentials"]
)
tenant_router.include_router(tenant_admin.router, prefix="/admin", tags=["admin"])


tenant_router.include_router(new_credentials.router, prefix="/holder", tags=["holder"])
