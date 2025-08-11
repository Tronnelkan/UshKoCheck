# app/main.py
import logging
import uvicorn
from fastapi import FastAPI, APIRouter
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka, FastapiProvider, inject, FromDishka
from starlette.staticfiles import StaticFiles

from app.api.v1.upload_endpoints import upload_router
from app.core.config import settings
from app.core.providers import DatabaseProvider, RepositoryProvider, ServiceProvider
from app.api.v1.user_endpoints import user_router

# Ліфеспан для закриття контейнера
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


def create_app():
    logging.basicConfig(level=logging.INFO)
    app = FastAPI(lifespan=lifespan)

    logging.info(f"DATABASE_URL = {settings.DATABASE_URL}")

    app.include_router(user_router)
    app.include_router(upload_router)

    container = make_async_container(
        DatabaseProvider(),
        RepositoryProvider(),
        ServiceProvider(),
        FastapiProvider(),  # для Depends(FromDishka[…])
    )

    # 3. Налаштовуємо FastAPI
    setup_dishka(container, app)
    app.state.dishka_container = container
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
