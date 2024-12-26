from typing import Iterable, Awaitable, Callable

from fastapi import FastAPI, Request, APIRouter, HTTPException, status

from application.exception.base import NotFound, ApplicationException
from application.layer import ApplicationLayer
from domain.layer import DomainLayer
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.layer import InfrastructureLayer
from infrastructure.settings.application import ApplicationSettings
from interface.web.routes.category.routes import router as category_router


class WebApplication:

    def __init__(
        self,
        layers: Iterable[Layer],
        routes: Iterable[APIRouter],
    ):
        self._container = Container()
        self._setup_layers(
            layers=layers,
        )
        self._app = self._create_application(
            routes=routes,
        )

    def _setup_layers(
        self,
        layers: Iterable[Layer],
    ) -> None:
        for layer in layers:
            layer.setup(container=self._container)

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

        @app.exception_handler(ApplicationException)
        def application_exception_handler(
            request: Request,  # noqa: ARG001
            exc: Exception,
        ) -> None:
            raise self._exception_factory(exception=exc)

        return app

    @staticmethod
    def _exception_factory(exception: Exception) -> HTTPException:
        match exception:
            case NotFound():
                return HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=str(exception),
                )

    def __call__(self):
        return self._app


web_app = WebApplication(
    layers=(
        InfrastructureLayer(),
        DomainLayer(),
        ApplicationLayer(),
    ),
    routes=(
        category_router,
    ),
)
