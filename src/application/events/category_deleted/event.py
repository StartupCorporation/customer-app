from pydantic import UUID4

from infrastructure.bus.impl.event.message import Event


class CategoryDeletedEvent(Event):
    id: UUID4

    @classmethod
    @property
    def __event_name__(cls) -> str:
        return "CATEGORY_DELETED"
