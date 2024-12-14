from abc import ABC, abstractmethod

from infrastructure.di.container import Container


class Module(ABC):

    @abstractmethod
    def setup(self, container: Container) -> None: ...
