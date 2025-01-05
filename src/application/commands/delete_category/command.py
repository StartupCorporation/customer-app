from pydantic import UUID4

from infrastructure.bus.command.message import Command


class DeleteCategoryCommand(Command):
    external_id: UUID4
