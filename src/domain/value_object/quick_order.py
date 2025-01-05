from dataclasses import dataclass

from domain.events.quick_order_created import QuickOrderCreated
from domain.exception.quick_order.client_name_is_not_alphabetic import ClientNameIsNotAlphabetic
from domain.exception.quick_order.phone_number_is_not_number import PhoneNumberIsNotNumberException
from domain.value_object.base import ValueObject


@dataclass(kw_only=True, slots=True)
class QuickOrder(ValueObject):
    customer: "QuickOrderCustomer"
    comment: str | None
    contact_me: bool

    def __post_init__(self):
        self._add_event(
            event=QuickOrderCreated.model_validate(self, from_attributes=True),
        )


@dataclass(kw_only=True, slots=True)
class QuickOrderCustomer:
    name: str
    phone: str
    email: str | None

    def __post_init__(self):
        self._check_phone()
        self._check_phone()

    def _check_name(self) -> None:
        if not self.name.isalpha():
            raise ClientNameIsNotAlphabetic()

    def _check_phone(self) -> None:
        if not self.phone.isdigit():
            raise PhoneNumberIsNotNumberException()
