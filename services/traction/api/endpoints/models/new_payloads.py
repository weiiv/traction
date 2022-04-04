from typing import Any, List
from pydantic import BaseModel
from uuid import UUID

from .new_basemodels import TimelineItem, Payload


class CredentialRead(Payload):
    credential: Any  # some adapter/type based on type
    credential_type: str  #'anoncred' or 'json-ld'


class CredentialGet(BaseModel):
    payload: CredentialRead
    timeline: List[TimelineItem]
    workflow_id: UUID | None


class VerifierPresenationGet(Payload):
    proof_request: Any
    presentation_request_type: str
    presentation_request_template_id: int
