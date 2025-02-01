from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


type GetProductDetailsQueryResult = ProductDetails


class ProductDetails(BaseModel):
    id: UUID
    name: str
    description: str
    quantity: int
    price: float
    images: list[str]
    comments: list["ProductDetailsComment"]


class ProductDetailsComment(BaseModel):
    author: str
    content: str
    created_at: datetime
