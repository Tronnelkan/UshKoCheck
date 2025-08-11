from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker, AsyncEngine,
)
from sqlalchemy.orm import declarative_base
from app.core.config import Settings

DATABASE_URL = Settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)

Base = declarative_base()


async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
