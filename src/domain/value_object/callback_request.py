from dataclasses import dataclass

from domain.events.callback_request_asked import CallbackRequestAsked, CallbackRequestAskedCustomerInput
from domain.exception.callback_request.client_name_is_not_alphabetic import ClientNameIsNotAlphabetic
from domain.value_object.base import ValueObject

from domain.value_object.phone_number import PhoneNumber


@dataclass(kw_only=True, slots=True)
class CallbackRequest(ValueObject):
    customer: "CallbackRequestCustomer"
    comment: str | None
    contact_me: bool

    def ask_for_callback_request(self) -> None:
        self._add_event(
            event=CallbackRequestAsked(
                comment=self.comment,
                contact_me=self.contact_me,
                customer=CallbackRequestAskedCustomerInput(
                    name=self.customer.name,
                    phone=self.customer.phone.number,
                ),
            ),
        )

    @classmethod
    def new(
        cls,
        comment: str | None,
        contact_me: bool,
        customer_name: str,
        customer_phone: str,
    ) -> "CallbackRequest":
        return CallbackRequest(
            comment=comment,
            contact_me=contact_me,
            customer=CallbackRequestCustomer.new(
                name=customer_name,
                phone=customer_phone,
            ),
        )


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
