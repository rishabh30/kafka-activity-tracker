from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import app.routers.users as users
import app.routers.activity_tracking as activity_tracking
from app.core.exceptions.base import CustomException
from app.core.middlewares.response_log import ResponseLogMiddleware

from app.kafka.consumer import KafkaMessageConsumer
from contextlib import asynccontextmanager
import asyncio
from app.db.init_db import setup_database


def init_routers(app_: FastAPI) -> None:
    app_.include_router(users.router, prefix="/user")
    app_.include_router(activity_tracking.router, prefix="/activity")


def init_listeners(app_: FastAPI) -> None:
    # Exception handler
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(ResponseLogMiddleware),
    ]
    return middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    consumer_manager = KafkaMessageConsumer()
    await consumer_manager.start()
    consumer_task = asyncio.create_task(consumer_manager.consume())

    yield

    await consumer_manager.stop()
    consumer_task.cancel()
    try:
        await consumer_task
    except asyncio.CancelledError:
        pass


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Activity Service",
        description="Activity Service API's",
        middleware=make_middleware(),
        lifespan=lifespan,
    )

    loop = asyncio.get_running_loop()
    if loop.is_running():
        loop.create_task(setup_database())
    else:
        asyncio.run(setup_database())
    init_routers(app_=app_)
    init_listeners(app_=app_)

    return app_


app = create_app()
