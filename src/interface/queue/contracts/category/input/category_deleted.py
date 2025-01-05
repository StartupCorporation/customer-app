import uuid
from typing import Annotated, Literal

from pydantic import BaseModel, UUID4, Field

from application.commands.delete_category.command import DeleteCategoryCommand
from interface.queue.contracts.base import MessageBrokerEvent


type CategoryDeletedInputContract = MessageBrokerEvent[Literal["CATEGORY_DELETED"], CategoryDeletedData]


class CategoryDeletedData(BaseModel):
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

    def to_command(self) -> DeleteCategoryCommand:
        return DeleteCategoryCommand(
            external_id=self.external_id,
        )
