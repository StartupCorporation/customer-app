from enum import StrEnum, auto
from typing import Annotated, NewType

from pydantic import Field, UUID4

from domain.entities.base import Entity
from domain.entities.product import Product


CategoryID = NewType("CategoryID", UUID4)


class Category(Entity[CategoryID]):
    name: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)]
    type: "CategoryType"

    products: list[Product]


class CategoryType(StrEnum):
    INVERTER = auto()
    ACCUMULATOR = auto()
    BMS = auto()
