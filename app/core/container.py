# app/core/container.py
from dishka import Provider, Scope, make_container
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.core.database import AsyncSessionLocal

# створюємо екземпляр провайдера
provider = Provider(scope=Scope.REQUEST)


@provider.provide(scope=Scope.REQUEST)
async def session() -> AsyncSession:
    async with AsyncSessionLocal() as s:
        yield s


provider.provide(UserRepository)
provider.provide(UserService)

container = make_container(provider)
