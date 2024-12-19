from infrastructure.bus.command.exception.base import CommandBusException


class CommandHandlerDoesNotExist(CommandBusException):

    def __init__(
        self,
        detail: str = "Command handler for the provided command doesn't exist.",
    ):
        super().__init__(detail)
