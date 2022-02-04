import json
import pytest, anyio
import asyncio
from httpx import AsyncClient

from tests.db.tenant_factory import TenantFactory
from api.db.repositories.tenants import TenantsRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_tenants_get_all(client: TestClient, session: AsyncSession) -> None:
    _repo = TenantsRepository(session)
    test_tenant = TenantFactory.build()
    print("==== test")
    print(anyio.get_current_task())
    print(hex(id(asyncio.get_running_loop())))
    print(session)
    session.add(test_tenant)
    # await session.commit()
    # async with AsyncClient(app=client.app, base_url="http://testserver") as ac:
    #     resp = await ac.get("/v1/tenants")
    #     assert resp.ok
    resp = await client.get("/v1/tenants")

    resp_content = json.loads(resp.content)

    assert len(resp_content) == 1
