from pydantic import BaseModel

from infrastructure.bus.command.message import Command


class AskForQuickOrderCommand(Command):
    customer: "AskForQuickOrderCommandCustomer"
    comment: str | None
    contact_me: bool


class AskForQuickOrderCommandCustomer(BaseModel):
    name: str
    phone: str
    email: str | None
