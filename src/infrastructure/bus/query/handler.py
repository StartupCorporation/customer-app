from abc import ABC, abstractmethod

from infrastructure.bus.base.handler import MessageHandler
from infrastructure.bus.query.message import Query


class QueryHandler[RESULT](MessageHandler[RESULT], ABC):

    @abstractmethod
    async def __call__(self, message: Query) -> RESULT: ...
