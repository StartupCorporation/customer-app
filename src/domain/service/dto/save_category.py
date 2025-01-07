from pydantic import BaseModel, UUID4


class SaveCategory(BaseModel):
    external_id: UUID4
    name: str
    description: str
    image: str
