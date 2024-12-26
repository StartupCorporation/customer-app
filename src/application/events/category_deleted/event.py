from pydantic import UUID4

from infrastructure.bus.event.message import Event


class CategoryDeletedEvent(Event):
    external_id: UUID4
