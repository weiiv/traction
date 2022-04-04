import logging
from typing import List, Any
from uuid import UUID
from pydantic import BaseModel

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.db.models.tenant import TenantRead
from api.endpoints.dependencies.db import get_db
from api.endpoints.models.new_payloads import CredentialGet


# /verifier/
router = APIRouter()
logger = logging.getLogger(__name__)


class CredRead(BaseModel):
    pass


@router.get("/", status_code=status.HTTP_200_OK, response_model=CredRead)
async def check_in_tenant(payload: Any, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


# TRACTION NATIVE OBJECT
# POST, PUT, DELETE
