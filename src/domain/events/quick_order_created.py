from pydantic import BaseModel

from domain.events.base import DomainEvent


class QuickOrderCreated(DomainEvent):
    customer: "QuickOrderCreatedCustomer"
    comment: str | None
    contact_me: bool


class QuickOrderCreatedCustomer(BaseModel):
    name: str
    phone: str
    email: str | None
