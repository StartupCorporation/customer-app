import uuid
from typing import Annotated

from pydantic import BaseModel, UUID4, Field

from application.events.category_saved.event import CategorySavedEvent


class CategorySavedInputContract(BaseModel):
    """
    Updates the existing category with the provided values.

    Otherwise, if the category with the provided `ID` doesn't exist, we will create it with the given values.
    """
    external_id: Annotated[
        UUID4,
        Field(
            validation_alias='id',
            examples=[uuid.uuid4()],
            description="The category `ID` from the admin application.",
        ),
    ]
    name: Annotated[
        str,
        Field(
            min_length=1,
            examples=["Accumulator"],
            description="The category name.",
        ),
    ]
    description: Annotated[
        str,
        Field(
            min_length=1,
            examples=["Accumulators are rechargeable energy storage devices."],
            description="The category description.",
        ),
    ]
    image: Annotated[
        str,
        Field(
            min_length=1,
            examples=["accumulator.png."],
            description="The image link of the category.",
        ),
    ]

    def to_event(self) -> CategorySavedEvent:
        return CategorySavedEvent(
            external_id=self.external_id,
            name=self.name,
            description=self.description,
            image=self.image,
        )