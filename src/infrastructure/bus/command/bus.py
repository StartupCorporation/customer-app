from typing import Callable, Awaitable, Iterable

from infrastructure.bus.command.handler import CommandHandler
from infrastructure.bus.command.message import Command
from infrastructure.bus.middleware.base import BusMiddleware


class CommandBus:

    def __init__(
        self,
        middlewares: Iterable[BusMiddleware] | None = None,
    ):
        self._handlers: list[type[Command]: CommandHandler] = {}
        self._middleware_chain: Callable[[Command], Awaitable[None]] = self._build_middleware_chain(
            middlewares=middlewares or [],
        )

    def register(self, message: type[Command], handler: CommandHandler) -> None:
        self._handlers[message] = handler

    async def handle(self, message: Command) -> None:
        await self._middleware_chain(message)

    def _build_middleware_chain(
        self,
        middlewares: Iterable[BusMiddleware],
    ) -> Callable[[Command], Awaitable[None]]:
        async def command_executor(message: Command) -> None:
            command_handler = self._handlers.get(message.__class__)

            if not command_handler:
                raise ValueError(f"Command handler doesn't exist for the '{message.__class__}' command")

            await command_handler(command=message)

        def wrapped_middleware(
            middleware: BusMiddleware,
            next_handler: Callable[[Command], Awaitable[None]],
        ) -> Callable[[Command], Awaitable[None]]:
            async def wrapped_handler(message: Command) -> None:
                return await middleware(
                    message=message,
                    next_=next_handler,  # type: ignore
                )

            return wrapped_handler

        for mdl in middlewares[::-1]:
            command_executor = wrapped_middleware(
                middleware=mdl,
                next_handler=command_executor,
            )

        return command_executor
