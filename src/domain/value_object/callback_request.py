from dataclasses import dataclass

from domain.exception.callback_request.client_name_is_not_alphabetic import ClientNameIsNotAlphabetic
from domain.exception.callback_request.comment_is_too_small import CommentIsTooSmall
from domain.value_object.base import ValueObject
from domain.value_object.phone_number import PhoneNumber


@dataclass(kw_only=True, slots=True)
class CallbackRequest(ValueObject):
    customer: "CallbackRequestCustomer"
    comment: str | None
    message_customer: bool

    @classmethod
    def new(
        cls,
        comment: str | None,
        message_customer: bool,
        customer_name: str,
        customer_phone: str,
    ) -> "CallbackRequest":
        return CallbackRequest(
            comment=comment,
            message_customer=message_customer,
            customer=CallbackRequestCustomer.new(
                name=customer_name,
                phone=customer_phone,
            ),
        )

    def __post_init__(self):
        self._check_comment()

    def ask_for_callback_request(self) -> None:
        from domain.events.callback_request_asked import CallbackRequestAsked

        self._add_event(
            event=CallbackRequestAsked(
                callback_request=self,
            ),
        )

    def _check_comment(self) -> None:
        if self.comment is not None and len(self.comment) < 10:
            raise CommentIsTooSmall()


@dataclass(kw_only=True, slots=True)
class CallbackRequestCustomer(ValueObject):
    name: str
    phone: PhoneNumber

    @classmethod
    def new(
        cls,
        name: str,
        phone: str,
    ) -> "CallbackRequestCustomer":
        return CallbackRequestCustomer(
            name=name,
            phone=PhoneNumber.new(
                number=phone,
            ),
        )

    def __post_init__(self):
        self._check_name()

    def _check_name(self) -> None:
        if not all(map(lambda v: v.isalpha(), self.name.split())):
            raise ClientNameIsNotAlphabetic()
