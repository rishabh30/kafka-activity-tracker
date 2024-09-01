from functools import lru_cache

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.db.config import DatabaseConfig

DATABASE_URL = f"postgresql+asyncpg://{DatabaseConfig.USERNAME}:{DatabaseConfig.PASSWORD}@{DatabaseConfig.HOSTNAME}:{DatabaseConfig.PORT}/{DatabaseConfig.DB}"


# Create an asynchronous engine
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Configure session factory to be used for creating database sessions
AsyncSession = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


from contextlib import asynccontextmanager


@asynccontextmanager
async def get_session():
    async with AsyncSession() as session:
        yield session


@lru_cache(maxsize=1)
def get_settings():
    session = get_session()
    return session
