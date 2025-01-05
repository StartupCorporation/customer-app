from abc import ABC, abstractmethod

from domain.events.base import DomainEvent
from infrastructure.bus.base.handler import MessageHandler


class EventSubscriber(MessageHandler[None], ABC):

    @abstractmethod
    async def __call__(self, message: DomainEvent) -> None: ...
