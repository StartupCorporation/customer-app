from typing import Iterable

from faststream import FastStream, ContextRepo
from faststream.broker.router import BrokerRouter
from faststream.rabbit import RabbitBroker

from application.layer import ApplicationLayer
from domain.layer import DomainLayer
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.layer import InfrastructureLayer
from infrastructure.settings.application import ApplicationSettings
from infrastructure.settings.rabbitmq import RabbitMQSettings
from interface.queue.routes import router


class QueueApplication:

    def __init__(
        self,
        layers: Iterable[Layer],
        routes: Iterable[BrokerRouter],
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
        routes: Iterable[BrokerRouter],
    ) -> FastStream:
        settings = self._container[ApplicationSettings]

        broker = RabbitBroker(self._container[RabbitMQSettings].connection_url)
        app = FastStream(
            broker=broker,
            title=settings.TITLE,
            version=settings.VERSION,
            description=f"**{settings.TITLE}** AsyncAPI documentation.",
        )

        for route in routes:
            broker.include_router(route)

        @app.on_startup
        def set_container_context(context: ContextRepo):
            context.set_global("container", self._container)

        return app

    def __call__(self):
        return self._app


queue_app = QueueApplication(
    layers=(
        InfrastructureLayer(),
        DomainLayer(),
        ApplicationLayer(),
    ),
    routes=(
        router,
    ),
)
