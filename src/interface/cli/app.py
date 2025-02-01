from typing import Iterable

from typer import Typer, Context

from application.layer import ApplicationLayer
from infrastructure.di.utils import get_di_container
from infrastructure.layer import InfrastructureLayer
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from interface.cli.subcommands.tl_outbox import app as tl_outbox


class CLIApplication:

    def __init__(
        self,
        container: Container,
        subcommands: Iterable[Typer],
    ) -> None:
        self._container = container
        self._app = self._create_application(
           subcommands=subcommands,
        )

    def _create_application(
        self,
        subcommands: Iterable[Typer],
    ) -> Typer:
        app = Typer()

        for command in subcommands:
            app.add_typer(
                typer_instance=command,
                name=command.info.name,
            )

        @app.callback()
        def set_registry(context: Context) -> None:
            context.obj = {
                "container": self._container,
            }

        return app

    def _setup_layers(
        self,
        layers: Iterable[Layer],
    ) -> None:
        for layer in layers:
            layer.setup(container=self._container)

    def __call__(self) -> Typer:
        return self._app()


if __name__ == "__main__":
    CLIApplication(
        container=get_di_container(
            layers=(
                InfrastructureLayer(),
                ApplicationLayer(),
            ),
        ),
        subcommands=(
           tl_outbox,
        ),
    )()
