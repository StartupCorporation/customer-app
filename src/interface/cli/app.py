from typing import Iterable

from typer import Typer, Context

from application.layer import ApplicationLayer
from domain.layer import DomainLayer
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.layer import InfrastructureLayer
from interface.cli.subcommands.queue import app as queue_app


class CLIApplication:

    def __init__(
        self,
        layers: Iterable[Layer],
        command_apps: Iterable[Typer],
    ) -> None:
        self._container = Container()
        self._layers = layers
        self._setup_modules()
        self._app = self._create_application(
            command_apps=command_apps,
        )

    def _setup_modules(self):
        for module in self._layers:
            module.setup(container=self._container)

    def _create_application(
        self,
        command_apps: Iterable[Typer],
    ) -> Typer:
        application = Typer()

        for command_app in command_apps:
            application.add_typer(command_app)

        @application.callback()
        def set_di_container(
            context: Context,
        ):
            context.obj = {
                "container": self._container,
            }

        return application

    def __call__(self) -> None:
        return self._app()


app = CLIApplication(
    layers=(
        InfrastructureLayer(),
        DomainLayer(),
        ApplicationLayer(),
    ),
    command_apps=(
        queue_app,
    ),
)

if __name__ == "__main__":
    app()
