from pydantic import UUID4

from infrastructure.bus.command.message import Command


class SaveProductCommand(Command):
    external_id: UUID4
    name: str
    description: str
    price: float
    quantity: int
    external_category_id: UUID4
    images: list[str]
