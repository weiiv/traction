import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Column, JSON, String
from sqlmodel import Field

from api.db.models.base import BaseModel, BaseTable

# just put any db models under the /catalog api here
# we think this will be moved to another service...


class OperationData(BaseModel):
    schema_name: Optional[str] = Field()
    schema_id: Optional[str] = Field()
    cred_def_id: Optional[str] = Field()


class OperationBase(BaseModel):
    name: str = Field(index=True, nullable=False)
    tags: List[str] = Field(default=[], sa_column=Column(ARRAY(String)))
    data: dict = Field(default={}, sa_column=Column(JSON))


class Operation(OperationBase, BaseTable, table=True):
    pass


class OperationCreate(OperationBase):
    data: Optional[OperationData] = None


class OperationRead(OperationBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    data: Optional[OperationData] = None


class OperationUpdate(BaseModel):
    id: uuid.UUID
    name: str
    tags: Optional[List[str]] = None
    data: Optional[OperationData] = None
