import logging
from typing import List, Any
from uuid import UUID
from pydantic import BaseModel

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.db.models.tenant import TenantRead
from api.endpoints.dependencies.db import get_db

# /holder/presentations
router = APIRouter()
logger = logging.getLogger(__name__)


class PresReqRead(BaseModel):
    pass


class HolderPresentationPropose(BaseModel):
    contact_id: UUID


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[PresReqRead])
async def check_in_tenant(payload: Any, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@router.get(
    "/{presentation_id}/creds",
    status_code=status.HTTP_200_OK,
    response_model=PresReqRead,
)
async def get_creds(db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@router.post(
    "/present-proof", status_code=status.HTTP_200_OK, response_model=PresReqRead
)
async def get_tenants(payload: Any, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@router.post("/reject", status_code=status.HTTP_200_OK, response_model=PresReqRead)
async def get_tenants(db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@router.post("/propose", status_code=status.HTTP_200_OK, response_model=PresReqRead)
async def get_tenants(
    payload: HolderPresentationPropose, db: AsyncSession = Depends(get_db)
):
    raise NotImplementedError
