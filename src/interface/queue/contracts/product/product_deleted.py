from typing import Annotated, Literal

from pydantic import BaseModel, UUID4, Field

from application.commands.delete_product.command import DeleteProductCommand
from interface.queue.contracts.base import MessageBrokerEvent


type ProductDeletedInputContract = MessageBrokerEvent[Literal["PRODUCT_DELETED"], ProductDeletedData]


class ProductDeletedData(BaseModel):
    external_id: Annotated[UUID4, Field(validation_alias='id')]

    def to_command(self) -> DeleteProductCommand:
        return DeleteProductCommand(
            external_id=self.external_id,
        )
