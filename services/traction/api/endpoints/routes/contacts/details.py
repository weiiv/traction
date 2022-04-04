import logging
from typing import List, Any
from uuid import UUID
from pydantic import BaseModel

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.db.models.tenant import TenantRead
from api.endpoints.dependencies.db import get_db


# /contacts/{contact_id}
router = APIRouter()
logger = logging.getLogger(__name__)


class Read(BaseModel):
    pass


@router.delete("/{contact_id}", status_code=status.HTTP_200_OK, response_model=Read)
async def delete_contacts(payload: Any, db: AsyncSession = Depends(get_db)):
    # soft-delete
    raise NotImplementedError


@router.get("/history", status_code=status.HTTP_200_OK, response_model=Read)
async def get_(contact_id: UUID, payload: Any, db: AsyncSession = Depends(get_db)):
    # return a collection of interactions (creds_recieved, creds_sent, proof_received, proof_sent, message_history)
    raise NotImplementedError
