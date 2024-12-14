from typing import Iterable, Awaitable, Callable

from fastapi import FastAPI, Request

from infrastructure import Container, ApplicationSettings, Module
from infrastructure.module import InfrastructureModule


class WebApplication:

    def __init__(
        self,
        modules: Iterable[Module],
    ):
        self._container = Container()
        self._modules = modules
        self._setup_modules()
        self._app = self._create_application()

    def _setup_modules(self):
        for module in self._modules:
            module.setup(container=self._container)

    def _create_application(self) -> FastAPI:
        app_settings = self._container[ApplicationSettings]
        app = FastAPI(
            debug=app_settings.DEBUG,
            description=app_settings.DESCRIPTION,
            version=app_settings.VERSION,
        )

        @app.middleware('http')
        async def set_registry[T](
            request: Request,
            call_next: Callable[[Request], Awaitable[T]],
        ) -> T:
            request.state.container = self._container
            return await call_next(request)

        return app

    def __call__(self):
        return self._app


web_app = WebApplication(
    modules=(
        InfrastructureModule(),
    ),
)
