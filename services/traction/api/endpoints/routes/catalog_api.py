import logging
from http.client import HTTPException
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.db.models.catalog import OperationRead, OperationCreate, OperationUpdate
from api.db.repositories.catalog import OperationRepository
from api.endpoints.dependencies.db import get_db


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(
    "/operations", status_code=status.HTTP_200_OK, response_model=List[OperationRead]
)
async def get_operations(
    tag: str | None = None, db: AsyncSession = Depends(get_db)
) -> List[OperationRead]:
    repo = OperationRepository(db_session=db)
    results = await repo.find_by_tag(tag=tag)
    return results


@router.post(
    "/operations", status_code=status.HTTP_200_OK, response_model=OperationRead
)
async def create_operation(
    payload: OperationCreate, db: AsyncSession = Depends(get_db)
) -> OperationRead:
    repo = OperationRepository(db_session=db)
    result = await repo.create(payload)
    return result


@router.get(
    "/operations/{operation_id}",
    status_code=status.HTTP_200_OK,
    response_model=OperationRead,
)
async def get_operation(
    operation_id: UUID, db: AsyncSession = Depends(get_db)
) -> OperationRead:
    repo = OperationRepository(db_session=db)
    result = await repo.get_by_id(operation_id)
    return result


@router.put(
    "/operations/{operation_id}",
    status_code=status.HTTP_200_OK,
    response_model=OperationRead,
)
async def update_operation(
    operation_id: UUID, payload: OperationUpdate, db: AsyncSession = Depends(get_db)
) -> OperationRead:
    repo = OperationRepository(db_session=db)
    current = await repo.get_by_id(operation_id)
    if current.id == payload.id:
        item = await repo.update(payload)
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Operation Id in payload does not match operation id in URL",
        )
