from pydantic import UUID4

from infrastructure.bus.impl.event.message import Event


class CategorySavedEvent(Event):
    id: UUID4
    name: str
    description: str
    image: str

    @classmethod
    @property
    def __event_name__(cls) -> str:
        return "CATEGORY_SAVED"
