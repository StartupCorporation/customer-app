from pydantic import UUID4

from infrastructure.bus.command.message import Command


class DeleteProductCommand(Command):
    external_id: UUID4
