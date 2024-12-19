from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


type GetProductDetailsQueryResult = ProductDetails


@dataclass(kw_only=True, slots=True, frozen=True)
class ProductDetails:
    id: UUID
    name: str
    description: str
    quantity: int
    price: float
    characteristics: dict
    images: list[str]
    comments: list["ProductDetailsComment"]


@dataclass(kw_only=True, slots=True, frozen=True)
class ProductDetailsComment:
    author: str
    content: str
    created_at: datetime
