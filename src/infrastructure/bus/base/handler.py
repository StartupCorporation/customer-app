from abc import ABC, abstractmethod

from infrastructure.bus.base.message import Message


class MessageHandler[RESULT](ABC):

    @abstractmethod
    async def __call__(self, message: Message) -> RESULT: ...
