from abc import ABC, abstractmethod

from domain.event_bus.event import ModelEvent


class EventSubscriber[EVENT: ModelEvent](ABC):

    @abstractmethod
    async def __call__(self, event: EVENT) -> None: ...
