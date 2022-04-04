import logging
from typing import List, Any
from uuid import UUID
from pydantic import BaseModel

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.db.models.tenant import TenantRead
from api.endpoints.dependencies.db import get_db


# /contacts
router = APIRouter()
logger = logging.getLogger(__name__)


class Read(BaseModel):
    pass


@router.get("/", status_code=status.HTTP_200_OK, response_model=Read)
async def get_contacts(payload: Any, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@router.post("/create-invitation", status_code=status.HTTP_200_OK, response_model=Read)
async def contact_create_invitation(
    db: AsyncSession = Depends(get_db),
) -> List[TenantRead]:
    raise NotImplementedError


@router.post("/receive-invitation", status_code=status.HTTP_200_OK, response_model=Read)
async def contact_recieve_invitation(
    db: AsyncSession = Depends(get_db),
) -> List[TenantRead]:
    raise NotImplementedError
