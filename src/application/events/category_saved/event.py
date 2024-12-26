from pydantic import UUID4

from infrastructure.bus.event.message import Event


class CategorySavedEvent(Event):
    external_id: UUID4
    name: str
    description: str
    image: str
