import logging

from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, AsyncEngine

from app.core.config import Settings
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

from typing import AsyncIterable


# 1️⃣ DB Provider
class DatabaseProvider(Provider):
    DATABASE_URL = Settings.DATABASE_URL.replace(
        "postgresql://", "postgresql+asyncpg://"
    )

    @provide(scope=Scope.APP)
    def get_engine(self) -> AsyncEngine:
        return create_async_engine(self.DATABASE_URL, echo=False)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, engine: AsyncEngine) -> AsyncIterable[AsyncSession]:
        SessionLocal = async_sessionmaker(
            bind=engine, expire_on_commit=False, autoflush=False
        )
        async with SessionLocal() as session:
            yield session


# 2️⃣ REPO PROVIDER
class RepositoryProvider(Provider):
    user_repo = provide(UserRepository, scope=Scope.REQUEST)


# 3️⃣ Service Provider
class ServiceProvider(Provider):
    user_service = provide(UserService, scope=Scope.REQUEST)
