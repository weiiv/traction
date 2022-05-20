import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.background import BackgroundTasks
from starlette.requests import Request

from api.core.config import settings
from api.endpoints.dependencies.db import get_db
from api.endpoints.dependencies.tenant_security import get_from_context
from api.endpoints.routes.v1.link_utils import build_list_links

from api.services.v1 import governance_service

from api.endpoints.models.v1.governance import (
    TemplateStatusType,
    CredentialTemplateListResponse,
    CredentialTemplateListParameters,
    CreateCredentialTemplatePayload,
    CreateCredentialTemplateResponse,
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=CredentialTemplateListResponse
)
async def list_credential_templates(
    request: Request,
    page_num: int | None = 1,
    page_size: int | None = settings.DEFAULT_PAGE_SIZE,
    name: str | None = None,
    cred_def_id: str | None = None,
    credential_template_id: UUID | None = None,
    schema_id: str | None = None,
    schema_template_id: UUID | None = None,
    status: TemplateStatusType | None = None,
    deleted: bool | None = False,
    db: AsyncSession = Depends(get_db),
) -> CredentialTemplateListResponse:
    wallet_id = get_from_context("TENANT_WALLET_ID")
    tenant_id = get_from_context("TENANT_ID")

    parameters = CredentialTemplateListParameters(
        url=str(request.url),
        page_num=page_num,
        page_size=page_size,
        name=name,
        deleted=deleted,
        cred_def_id=cred_def_id,
        credential_template_id=credential_template_id,
        schema_id=schema_id,
        schema_template_id=schema_template_id,
        status=status,
    )
    items, total_count = await governance_service.list_credential_templates(
        db, tenant_id, wallet_id, parameters
    )

    links = build_list_links(total_count, parameters)

    return CredentialTemplateListResponse(
        items=items, count=len(items), total=total_count, links=links
    )


@router.post("/", status_code=status.HTTP_200_OK)
async def create_credential_template(
    payload: CreateCredentialTemplatePayload,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
) -> CreateCredentialTemplateResponse:
    wallet_id = get_from_context("TENANT_WALLET_ID")
    tenant_id = get_from_context("TENANT_ID")

    item = await governance_service.create_credential_template(
        db, tenant_id, wallet_id, payload=payload
    )
    links = []  # TODO

    # this will kick off the call to the ledger and then event listeners will finish
    # populating the schema (and cred def) data.
    background_tasks.add_task(
        governance_service.send_cred_def_request_task,
        db=db,
        tenant_id=tenant_id,
        credential_template_id=item.credential_template_id,
    )

    return CreateCredentialTemplateResponse(item=item, links=links)
