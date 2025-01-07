from pydantic import BaseModel

from domain.events.base import DomainEvent


class CallbackRequestAsked(DomainEvent):
    customer: "CallbackRequestAskedCustomerInput"
    comment: str | None
    contact_me: bool


class CallbackRequestAskedCustomerInput(BaseModel):
    name: str
    phone: str
