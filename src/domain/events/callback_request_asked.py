from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar
from uuid import UUID

from domain.event_bus.event import IntegrationEvent
from domain.value_object.callback_request import CallbackRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class CallbackRequestAsked(IntegrationEvent):
    __event_name__: ClassVar[str] = "CALLBACK_REQUEST_ASKED"

    callback_request: "CallbackRequest"

    def serialize(self) -> dict:
        return {
            "id": str(self.__event_id__),
            "created_at": str(self.__event_created_at__),
            "event_type": self.__event_name__,
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
            __event_id__=UUID(data['id']),
            __event_created_at__=datetime.fromisoformat(data['created_at']),
            callback_request=CallbackRequest.new(
                comment=data['data']['comment'],
                message_customer=data['data']['message_customer'],
                customer_name=data['data']['customer']['name'],
                customer_phone=data['data']['customer']['phone'],
            ),
        )
