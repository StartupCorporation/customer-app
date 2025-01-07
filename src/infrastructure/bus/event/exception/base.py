from infrastructure.exception import InfrastructureException


class EventBusException(InfrastructureException):

    def __init__(
        self,
        detail: str = "Exception has been happened in the event_bus bus.",
    ):
        super().__init__(detail)
