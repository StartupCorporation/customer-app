from abc import ABC, abstractmethod

from infrastructure.bus.base.handler import MessageHandler
from infrastructure.bus.base.message import Message


class MessageBus[RESULT](ABC):

    @abstractmethod
    def register(self, message: type[Message], handler: MessageHandler) -> None: ...

    @abstractmethod
    async def handle(self, message: Message) -> RESULT: ...
