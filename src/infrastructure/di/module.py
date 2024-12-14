from abc import ABC, abstractmethod

from infrastructure import Container


class Module(ABC):

    @abstractmethod
    def setup(self, container: Container) -> None: ...
