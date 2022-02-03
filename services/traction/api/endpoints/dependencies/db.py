from sqlalchemy.ext.asyncio import AsyncSession

from api.db.session import async_session


async def get_db() -> AsyncSession:
    """
    Dependency function that yields db sessions
    """
    print("regular get_db")
    async with async_session() as session:
        yield session
        await session.commit()
