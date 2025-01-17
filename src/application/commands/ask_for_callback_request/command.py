from infrastructure.bus.command.message import Command


class AskForCallbackRequestCommand(Command):
    customer_name: str
    customer_phone: str
    comment: str | None
    message_customer: bool
