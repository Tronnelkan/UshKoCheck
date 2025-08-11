import datetime
from typing import Optional, List

from app.models.tables import Users
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserUpdate


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(self, data: UserCreate) -> Users:
        return await self.repo.create(data=data)

    async def get_user(self, id_telegram: int) -> Optional[Users]:
        return await self.repo.get(id_telegram=id_telegram)

    async def get_all_users(self) -> List[Users]:
        return await self.repo.get_all()

    async def update_user(self, data: UserUpdate) -> Users:
        return await self.repo.update(data=data)

    async def delete_user(self, id_telegram: int) -> Users:
        return await self.repo.delete(id_telegram=id_telegram)

    async def delete_all_users(self) -> None:
        await self.repo.delete_all()
