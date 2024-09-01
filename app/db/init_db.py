import asyncpg
from app.models.user import Base as UserModelsBase
from app.models.activity import Base as ActivityTrackingBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.db.config import DatabaseConfig

DATABASE_URL = f"postgresql+asyncpg://{DatabaseConfig.USERNAME}:{DatabaseConfig.PASSWORD}@{DatabaseConfig.HOSTNAME}:{DatabaseConfig.PORT}/"
DATABASE_NAME = f"{DatabaseConfig.DB}"


async def create_database_if_not_exists():
    """
    Connects to the PostgreSQL server and creates a new database if it does not already exist.
    """
    dsn = f"postgresql://{DatabaseConfig.USERNAME}:{DatabaseConfig.PASSWORD}@{DatabaseConfig.HOSTNAME}:{DatabaseConfig.PORT}/"
    conn = await asyncpg.connect(dsn=dsn)
    try:
        result = await conn.fetchrow(
            "SELECT 1 FROM pg_database WHERE datname = $1", DATABASE_NAME
        )
        if not result:
            await conn.execute(f"CREATE DATABASE {DATABASE_NAME}")
    finally:
        await conn.close()


async def setup_database():
    """
    Sets up the database and all tables defined.
    """
    await create_database_if_not_exists()

    engine: AsyncEngine = create_async_engine(
        f"{DATABASE_URL}{DATABASE_NAME}", echo=True
    )

    async with engine.begin() as conn:
        await conn.run_sync(UserModelsBase.metadata.create_all)
        await conn.run_sync(ActivityTrackingBase.metadata.create_all)

    await engine.dispose()
