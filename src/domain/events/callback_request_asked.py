from pydantic import BaseModel

from domain.events.base import DomainEvent


class CallbackRequestAsked(DomainEvent):
    customer: "CallbackRequestAskedCustomerInput"
    comment: str | None
    message_customer: bool


class CallbackRequestAskedCustomerInput(BaseModel):
    name: str
    phone: str
