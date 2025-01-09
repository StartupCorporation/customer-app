from abc import ABC, abstractmethod

from infrastructure.bus.query.message import Query


class QueryHandler[QUERY: Query, RESULT](ABC):

    @abstractmethod
    async def __call__(self, query: QUERY) -> RESULT: ...
