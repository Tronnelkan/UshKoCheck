from typing import Optional, List

from sqlalchemy import select, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tables import Users
from app.schemas.user_schemas import UserCreate, UserUpdate


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: UserCreate) -> Users:
        result = await self.session.execute(
            select(Users).where(Users.id_telegram == data.id_telegram)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user:
            return existing_user

        user = Users(**data.dict())
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def get(self, id_telegram: int) -> Optional[Users]:
        result = await self.session.execute(select(Users).where(Users.id_telegram == id_telegram))

        return result.scalar_one_or_none()

    async def get_all(self) -> List[Users]:
        result = await self.session.execute(select(Users))

        return result.scalars().all()

    async def update(self, data: UserUpdate) -> Users:
        stmt = select(Users).where(Users.id_telegram == data.id_telegram)

        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            raise NoResultFound(f"User {data.id_telegram} not found")

        for field, value in data.dict().items():
            setattr(user, field, value)

        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete(self, id_telegram: int) -> Users:
        result = await self.session.execute(select(Users).where(Users.id_telegram == id_telegram))

        user = result.scalar_one_or_none()

        if user:
            await self.session.delete(user)
            await self.session.commit()

        return user

    async def delete_all(self) -> None:
        await self.session.execute(delete(Users))
        await self.session.commit()
