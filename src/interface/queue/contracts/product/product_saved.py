from typing import Annotated, Literal

from pydantic import BaseModel, UUID4, Field

from application.commands.save_product.command import SaveProductCommand
from interface.queue.contracts.base import MessageBrokerEvent


type ProductSavedInputContract = MessageBrokerEvent[Literal["PRODUCT_SAVED"], ProductSavedData]


class ProductSavedData(BaseModel):
    external_id: Annotated[UUID4, Field(validation_alias='id')]
    name: str
    description: str
    price: float
    stock_quantity: int
    external_category_id: Annotated[UUID4, Field(validation_alias='category_id')]
    images: list[str]

    def to_command(self) -> SaveProductCommand:
        return SaveProductCommand(
            external_id=self.external_id,
            name=self.name,
            description=self.description,
            price=self.price,
            quantity=self.stock_quantity,
            external_category_id=self.external_category_id,
            images=self.images,
        )
