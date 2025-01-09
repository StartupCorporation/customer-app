from abc import ABC, abstractmethod
from typing import Callable, Awaitable

from domain.event_bus.event import ModelEvent


class ModelEventBus(ABC):

    @abstractmethod
    async def publish(self, event: ModelEvent) -> None: ...

    @abstractmethod
    def register(self, event: type[ModelEvent], subscriber: Callable[[ModelEvent], Awaitable[None]]) -> None: ...
