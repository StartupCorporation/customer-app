from typing import Iterable, Awaitable, Callable

from fastapi import FastAPI, Request, APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from application.exception.base import NotFound
from application.layer import ApplicationLayer
from domain.exception.base import DomainException
from infrastructure.di.container import Container
from infrastructure.di.utils import get_di_container
from infrastructure.layer import InfrastructureLayer
from infrastructure.settings.application import ApplicationSettings
from interface.web.routes.callback_request.routes import router as callback_request_router
from interface.web.routes.category.routes import router as category_router


class WebApplication:

    def __init__(
        self,
        container: Container,
        routes: Iterable[APIRouter],
    ):
        self._container = container
        self._app = self._create_application(
            routes=routes,
        )

    def _create_application(
        self,
        routes: Iterable[APIRouter],
    ) -> FastAPI:
        settings = self._container[ApplicationSettings]

        app = FastAPI(
            title=settings.TITLE,
            debug=settings.DEBUG,
            version=settings.VERSION,
            description=f"**{settings.TITLE}** OpenAPI documentation.",
            docs_url="/docs" if settings.DEBUG else None,
        )

        for route in routes:
            app.include_router(route)

        @app.middleware('http')
        async def set_registry[T](
            request: Request,
            call_next: Callable[[Request], Awaitable[T]],
        ) -> T:
            request.state.container = self._container
            return await call_next(request)

        @app.middleware("http")
        async def exception_handling_middleware(request: Request, call_next):
            try:
                return await call_next(request)
            except Exception as e:
                return self._exception_factory(exception=e)

        app.add_middleware(
            CORSMiddleware,  # type: ignore
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        return app

    def _exception_factory(self, exception: Exception) -> JSONResponse:
        match exception:
            case NotFound():
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={"detail": str(exception)},
                )
            case DomainException():
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={"detail": str(exception)},
                )
            case Exception() if self._container[ApplicationSettings].DEBUG:
                raise exception
            case Exception():
                return JSONResponse(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    content={"detail": "Something went wrong..."},
                )

    def __call__(self):
        return self._app


web_app = WebApplication(
    container=get_di_container(
        layers=(
            InfrastructureLayer(),
            ApplicationLayer(),
        ),
    ),
    routes=(
        category_router,
        callback_request_router,
    ),
)
