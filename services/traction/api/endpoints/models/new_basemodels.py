from typing import Any, List
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class TimelineItem(BaseModel):
    event_time: datetime
    event_state: str
    description: str | None
    acapy_item_id: UUID
    protocol_type: str


class Payload(BaseModel):
    contact_id: UUID
    contact_name: str
    updated_at: datetime
    acapy_item_id: UUID
    state: str | None
