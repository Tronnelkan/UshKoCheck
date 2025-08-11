from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends

from app.schemas.user_schemas import UserCreate, UserUpdate
from app.services.user_service import UserService

user_router = APIRouter(prefix="/users")


@user_router.post("/create")
@inject
async def create_user(
        user_data: UserCreate,
        user_service: FromDishka[UserService],
):
    return await user_service.create_user(user_data)


@user_router.get("/get/{id_telegram}")
@inject
async def get_user(
        id_telegram: int,
        user_service: FromDishka[UserService]
):
    return await user_service.get_user(id_telegram=id_telegram)


@user_router.get("/get_all")
@inject
async def get_all_users(
        user_service: FromDishka[UserService]
):
    return await user_service.get_all_users()


@user_router.put("/update")
@inject
async def update_user(
        user_data: UserUpdate,
        user_service: FromDishka[UserService]
):
    return await user_service.update_user(data=user_data)


@user_router.delete("/delete/{id_telegram}")
@inject
async def delete_user(
        id_telegram: int,
        user_service: FromDishka[UserService]
):
    return await user_service.delete_user(id_telegram=id_telegram)


@user_router.delete("/delete_all")
@inject
async def delete_all_users(
        user_service: FromDishka[UserService]
):
    await user_service.delete_all_users()
