from abc import ABC, abstractmethod

from infrastructure.bus.base.handler import MessageHandler
from infrastructure.bus.event.message import Event


class EventHandler(MessageHandler[None], ABC):

    @abstractmethod
    async def __call__(self, message: Event) -> None: ...
