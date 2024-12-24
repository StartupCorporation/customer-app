from typing import Callable, Awaitable, Any

from infrastructure.bus.base.message import Message
from infrastructure.bus.base.middleware import MessageHandlerMiddleware
from infrastructure.database.relational.transaction import TransactionManager


class TransactionMiddleware[RESULT](MessageHandlerMiddleware[RESULT]):

    def __init__(
        self,
        transaction_manager: TransactionManager,
    ):
        self._transaction_manager = transaction_manager

    async def __call__(
        self,
        message: Message,
        next_: Callable[[Message], Awaitable[Any]],
    ) -> RESULT:
        async with self._transaction_manager.begin():
            return await next_(message)
