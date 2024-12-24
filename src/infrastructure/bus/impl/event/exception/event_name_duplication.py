from infrastructure.bus.impl.event.exception.base import EventBusException


class EventNameDuplication(EventBusException):

    def __init__(
        self,
        detail: str = "Event's name is already existing. Choose another name.",
    ):
        super().__init__(detail)
