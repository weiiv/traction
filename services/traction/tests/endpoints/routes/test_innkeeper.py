import json

from tests.db.tenant_factory import TenantFactory
from api.db.repositories.tenants import TenantsRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.testclient import TestClient


async def test_tenants_get_all(
    client: TestClient, session: AsyncSession, event_loop
) -> None:
    _repo = TenantsRepository(session)
    test_tenant = TenantFactory.build()
    session.add(test_tenant)

    resp = client.get("/v1/tenants")

    assert resp.ok
    resp_content = json.loads(resp.content)

    assert len(resp_content) == 1
