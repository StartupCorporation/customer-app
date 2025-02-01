from typing import Annotated, Literal

from pydantic import BaseModel, UUID4, Field

from application.commands.save_category.command import SaveCategoryCommand
from interface.queue.contracts.base import MessageBrokerEvent


type CategorySavedInputContract = MessageBrokerEvent[Literal["CATEGORY_SAVED"], CategorySavedData]


class CategorySavedData(BaseModel):
    external_id: Annotated[UUID4, Field(validation_alias='id')]
    name: str
    description: str
    image: str

    def to_command(self) -> SaveCategoryCommand:
        return SaveCategoryCommand(
            external_id=self.external_id,
            name=self.name,
            description=self.description,
            image=self.image,
        )
