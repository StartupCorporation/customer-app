import uuid
from typing import Annotated

from pydantic import BaseModel, UUID4, Field

from application.events.category_deleted.event import CategoryDeletedEvent


class CategoryDeletedInputContract(BaseModel):
    """
    Deletes a category with the provided `ID` field.
    """
    external_id: Annotated[
        UUID4,
        Field(
            validation_alias='id',
            examples=[uuid.uuid4()],
            description="The category `ID` from the admin application.",
        ),
    ]

    def to_event(self) -> CategoryDeletedEvent:
        return CategoryDeletedEvent(
            external_id=self.external_id,
        )
