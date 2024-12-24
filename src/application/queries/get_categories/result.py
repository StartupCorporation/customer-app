from pydantic import BaseModel, UUID4


type CategoryQueryResult = list[CategoryData]


class CategoryData(BaseModel):
    id: UUID4
    name: str
    description: str
    image: str
