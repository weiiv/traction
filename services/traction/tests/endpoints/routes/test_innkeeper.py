import asyncio
import pytest
import json
import pprint


from tests.db.tenant_factory import TenantFactory
from api.db.repositories.tenants import TenantsRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.testclient import TestClient

from fastapi import APIRouter, Depends
from api.endpoints.dependencies.db import get_db


pp = pprint.PrettyPrinter()


def test_tenants_get_all(
    client: TestClient, session: AsyncSession, db=Depends(get_db)
) -> None:
    print("test client")
    print(client)
    print("test session")
    print(session)

    _repo = TenantsRepository(session)

    test_tenant = TenantFactory.build()
    session.add(test_tenant)
    # pp.pprint(_repo.find())
    print(client)
    pp.pprint(client.app.__dict__)
    resp = client.get("/innkeeper/v1/tenants")

    assert resp.ok
    resp_content = json.loads(resp.content)

    assert len(resp_content) == 1
