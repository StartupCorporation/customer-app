from pydantic import BaseModel, UUID4


type GetCategoryProductsQueryResult = list[CategoryProduct]


class CategoryProduct(BaseModel):
    id: UUID4
    name: str
    images: list[str]
