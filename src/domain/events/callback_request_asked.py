import json
from dataclasses import dataclass
from typing import TYPE_CHECKING

from domain.event_bus.event import IntegrationEvent


if TYPE_CHECKING:
    from domain.value_object.callback_request import CallbackRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class CallbackRequestAsked(IntegrationEvent):
    callback_request: "CallbackRequest"

    def serialize(self) -> bytes:
        return json.dumps(
            {
                "id": str(self._id),
                "created_at": str(self._created_at),
                "event_type": "CALLBACK_REQUEST_ASKED",
                "data": {
                    "customer": {
                        "name": self.callback_request.customer.name,
                        "phone": self.callback_request.customer.phone.number,
                    },
                    "comment": self.callback_request.comment,
                    "message_customer": self.callback_request.message_customer,
                },
            },
        ).encode()
