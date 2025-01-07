from typing import Any

from infrastructure.bus.base.bus import MessageBus
from infrastructure.bus.query.handler import QueryHandler
from infrastructure.bus.query.message import Query


class QueryBus(MessageBus[Any]):

    def __init__(self):
        self._handlers = {}

    def register(self, message: type[Query], handler: QueryHandler) -> None:
        self._handlers[message] = handler

    async def handle(self, message: Query) -> Any:
        query_handler = self._handlers.get(message.__class__)

        if not query_handler:
            raise ValueError(f"Query handler doesn't exist for the '{message.__class__}' query")

        return await query_handler(message)
