from pydantic import UUID4

from infrastructure.bus.command.message import Command


class SaveCategoryCommand(Command):
    external_id: UUID4
    name: str
    description: str
    image: str
