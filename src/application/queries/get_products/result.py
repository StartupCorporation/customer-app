from pydantic import BaseModel, UUID4


type GetProductsQueryResult = list[ProductShortInfo]


class ProductShortInfo(BaseModel):
    id: UUID4
    category_id: UUID4
    name: str
    price: float
    images: list[str]
