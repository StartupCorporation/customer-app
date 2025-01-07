import uuid
from typing import Annotated, Literal

from pydantic import BaseModel, UUID4, Field

from application.commands.save_category.command import SaveCategoryCommand
from interface.queue.contracts.base import MessageBrokerEvent


type CategorySavedInputContract = MessageBrokerEvent[Literal["CATEGORY_SAVED"], CategorySavedData]


class CategorySavedData(BaseModel):
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

    def to_command(self) -> SaveCategoryCommand:
        return SaveCategoryCommand(
            external_id=self.external_id,
            name=self.name,
            description=self.description,
            image=self.image,
        )
