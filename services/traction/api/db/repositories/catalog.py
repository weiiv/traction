from typing import List, Type
from pydantic import parse_obj_as
from sqlalchemy import func, select
from api.db.models.catalog import (
    OperationCreate,
    OperationUpdate,
    OperationRead,
    Operation,
)
from api.db.repositories.base import BaseRepository


class OperationRepository(
    BaseRepository[
        OperationCreate,
        OperationUpdate,
        OperationRead,
        Operation,
    ]
):
    @property
    def _in_schema(self) -> Type[OperationCreate]:
        return OperationCreate

    @property
    def _upd_schema(self) -> Type[OperationUpdate]:
        return OperationUpdate

    @property
    def _schema(self) -> Type[OperationRead]:
        return OperationRead

    @property
    def _table(self) -> Type[Operation]:
        return Operation

    async def find_by_tag(
        self, tag: str, offset: int = 0, limit: int = 100
    ) -> List[OperationRead]:
        like_tag = "%" if tag is None or tag == "" else f"%{tag}%"
        q = (
            select(self._table)
            .filter(
                func.array_to_string(self._table.tags, ",").ilike(func.any_([like_tag]))
            )
            .offset(offset)
            .limit(limit)
        )
        result = await self._db_session.execute(q)
        items = result.scalars().all()
        return parse_obj_as(List[OperationRead], items)
