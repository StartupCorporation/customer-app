from dataclasses import dataclass
from uuid import UUID


type CategoryQueryResult = list[CategoryData]


@dataclass(frozen=True, kw_only=True, slots=True)
class CategoryData:
    id: UUID
    name: str
    description: str
    image: str
