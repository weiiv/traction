import pytest_asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.testclient import TestClient

from api.main import app
from api.db.session import engine
from api.endpoints.dependencies.db import get_db
from sqlalchemy.orm import sessionmaker

TestingSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


"""
def test_get_db() -> AsyncSession:
    with async_session() as session:
        txn = session.begin_nested()
        yield session
        txn.rollback()


@pytest_asyncio.fixture
async def test_session() -> AsyncSession:
    fixed_test_session = next(test_get_db())
    print(fixed_test_session)
    while True:
        yield fixed_test_session


@pytest_asyncio.fixture
async def client(test_session) -> TestClient:
    app.dependency_overrides[get_db] = test_session
    client = TestClient(app)
    return client

"""
# This fixture is the main difference to before. It creates a nested
# transaction, recreates it when the application code calls session.commit
# and rolls it back at the end.
# Based on: https://docs.sqlalchemy.org/en/14/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites
@pytest_asyncio.fixture()
async def session():
    connection = await engine.connect()
    transaction = await connection.begin()
    session = TestingSessionLocal(bind=connection)

    # Begin a nested transaction (using SAVEPOINT).
    # nested = connection.begin_nested()

    # # If the application code calls session.commit, it will end the nested
    # # transaction. Need to start a new one when that happens.
    # @sa.event.listens_for(session, "after_transaction_end")
    # def end_savepoint(session, transaction):
    #     nonlocal nested
    #     if not nested.is_active:
    #         nested = connection.begin_nested()
    print("session fixture")
    print(session)
    yield session

    # Rollback the overall transaction, restoring the state before the test ran.
    await session.close()
    # await transaction.rollback()
    await connection.close()


# A fixture for the fastapi test client which depends on the
# previous session fixture. Instead of creating a new session in the
# dependency override as before, it uses the one provided by the
# session fixture.
@pytest_asyncio.fixture()
async def client(session):
    print("client fixture")
    print(session)

    def override_get_db():
        print("override session")
        yield session

    test_app = TestClient(app)
    app.dependency_overrides[get_db] = override_get_db
    print("run_override")
    print(app.dependency_overrides[get_db])
    print("yeilded client")
    print(test_app)
    yield test_app
    del app.dependency_overrides[get_db]
