from typing import Iterable

from infrastructure.di.container import Container
from infrastructure.di.layer import Layer


def get_di_container(
    layers: Iterable[Layer],
) -> Container:
    container = Container()

    for layer in layers:
        layer.setup(
            container=container,
        )

    return container
