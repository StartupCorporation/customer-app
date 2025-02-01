from typing import Annotated, Literal

from pydantic import BaseModel, UUID4, Field

from application.commands.delete_category.command import DeleteCategoryCommand
from interface.queue.contracts.base import MessageBrokerEvent


type CategoryDeletedInputContract = MessageBrokerEvent[Literal["CATEGORY_DELETED"], CategoryDeletedData]


class CategoryDeletedData(BaseModel):
    external_id: Annotated[UUID4, Field(validation_alias='id')]

    def to_command(self) -> DeleteCategoryCommand:
        return DeleteCategoryCommand(
            external_id=self.external_id,
        )
