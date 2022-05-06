from fastapi import APIRouter

from .contacts import contacts_router
from .invitations import invitations_router

v1_tenant_router = APIRouter()
v1_tenant_router.include_router(contacts_router, prefix="/contacts", tags=["contacts"])
v1_tenant_router.include_router(
    invitations_router, prefix="/invitations", tags=["invitations"]
)
