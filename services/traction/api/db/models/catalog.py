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
    schema_name: str = Field()
    schema_id: str = Field()
    cred_def_id: str = Field()


class OperationBase(BaseModel):
    name: str = Field(index=True, nullable=False)
    tags: List[str] = Field(default=[], sa_column=Column(ARRAY(String)))
    data: dict = Field(default={}, sa_column=Column(JSON))


class Operation(OperationBase, BaseTable, table=True):
    # This is the class that represents the table
    # this will have id, created_at, updated_at from BaseTable
    # and fields from OperationBase
    # this should fully represent the table
    pass


class OperationCreate(OperationBase):
    # This is the class that represents interface for creating a tenant
    # we must set all the required fields,
    data: Optional[OperationData] = None


class OperationRead(OperationBase):
    # This is the class that represents interface for reading a operation
    # here we indicate id, created_at and updated_at must be included
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    data: Optional[OperationData] = None


class OperationUpdate(BaseModel):
    # This is our update interface
    # This does NOT inherit from OperationBase,
    # so no need to worry about accidentally updating id or other fields
    name: Optional[str] = None
    tags: Optional[List[str]] = None
    data: Optional[OperationData] = None
