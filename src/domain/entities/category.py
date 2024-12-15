from enum import StrEnum, auto
from typing import Annotated, NewType

from pydantic import Field, UUID4

from domain.entities.base import Entity
from domain.entities.product import Product
from domain.exception.product.invalid_image_link import InvalidImageLink


CategoryID = NewType("CategoryID", UUID4)


class Category(Entity[CategoryID]):
    name: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)]
    type: "CategoryType"
    image_link: Annotated[str, Field(min_length=1)]

    products: list[Product]

    def set_new_image(
        self,
        image_link: str,
    ) -> None:
        if not image_link:
            raise InvalidImageLink(
                "Image link cannot be zero-length."
            )

        self.image_link = image_link


class CategoryType(StrEnum):
    INVERTER = auto()
    ACCUMULATOR = auto()
    BMS = auto()
