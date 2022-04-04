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


# /holder/credentials
router = APIRouter()
logger = logging.getLogger(__name__)


class CredRead(BaseModel):
    pass


@router.get("/", status_code=status.HTTP_200_OK, response_model=CredentialGet)
async def holder_get_creds(payload: Any, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@router.post("/accept-offer", status_code=status.HTTP_200_OK, response_model=CredRead)
async def holder_accept_cred_offer(
    db: AsyncSession = Depends(get_db),
) -> List[TenantRead]:
    raise NotImplementedError


@router.post("/reject-offer", status_code=status.HTTP_200_OK, response_model=CredRead)
async def holder_reject_cred_offer(
    db: AsyncSession = Depends(get_db),
) -> List[TenantRead]:
    raise NotImplementedError


@router.delete("/{credential_id}")
async def delete_credential(db: AsyncSession = Depends(get_db)):
    raise NotImplementedError
