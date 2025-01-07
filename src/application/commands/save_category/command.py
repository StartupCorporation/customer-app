from pydantic import UUID4

from domain.service.dto.save_category import SaveCategory
from infrastructure.bus.command.message import Command


class SaveCategoryCommand(Command):
    external_id: UUID4
    name: str
    description: str
    image: str

    def to_dto(self) -> SaveCategory:
        return SaveCategory(
            external_id=self.external_id,
            name=self.name,
            description=self.description,
            image=self.image,
        )
