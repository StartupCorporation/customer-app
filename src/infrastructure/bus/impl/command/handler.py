from abc import ABC, abstractmethod

from infrastructure.bus.base.handler import MessageHandler
from infrastructure.bus.impl.command.message import Command


class CommandHandler(MessageHandler[None], ABC):

    @abstractmethod
    async def __call__(self, message: Command) -> None: ...
