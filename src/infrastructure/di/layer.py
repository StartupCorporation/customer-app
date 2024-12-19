from abc import ABC, abstractmethod

from infrastructure.di.container import Container


class Layer(ABC):

    @abstractmethod
    def setup(self, container: Container) -> None: ...
