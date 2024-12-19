from dataclasses import dataclass
from uuid import UUID


type GetCategoryProductsQueryResult = list[CategoryProduct]


@dataclass(kw_only=True, slots=True, frozen=True)
class CategoryProduct:
    id: UUID
    name: str
    images: list[str]
