from infrastructure.exception import InfrastructureException


class CommandBusException(InfrastructureException):

    def __init__(
        self,
        detail: str = "Exception has been happened in the command bus."
    ):
        super().__init__(detail)
