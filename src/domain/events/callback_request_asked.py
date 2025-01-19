from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from domain.event_bus.event import IntegrationEvent


if TYPE_CHECKING:
    from domain.value_object.callback_request import CallbackRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class CallbackRequestAsked(IntegrationEvent):
    callback_request: "CallbackRequest"

    def serialize(self) -> dict:
        return {
            "id": str(self.event_id),
            "created_at": str(self.event_created_at),
            "event_type": self.event_type,
            "data": {
                "customer": {
                    "name": self.callback_request.customer.name,
                    "phone": self.callback_request.customer.phone.number,
                },
                "comment": self.callback_request.comment,
                "message_customer": self.callback_request.message_customer,
            },
        }

    @classmethod
    def deserialize(cls, data: dict) -> "CallbackRequestAsked":
        return CallbackRequestAsked(
            event_id=UUID(data['event_id']),
            event_created_at=datetime.fromisoformat(data['event_created_at']),
            callback_request=CallbackRequest.new(
                comment=data['comment'],
                message_customer=data['message_customer'],
                customer_name=data['customer']['name'],
                customer_phone=data['customer']['phone'],
            ),
        )

    @property
    def event_type(self) -> str:
        return "CALLBACK_REQUEST_ASKED"
