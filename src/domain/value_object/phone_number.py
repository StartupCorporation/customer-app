from dataclasses import dataclass

import phonenumbers

from domain.exception.phone_number.phone_number_is_invalid import PhoneNumberIsInvalid
from domain.value_object.base import ValueObject


@dataclass(kw_only=True, slots=True)
class PhoneNumber(ValueObject):
    number: str

    @classmethod
    def new(
        cls,
        number: str,
    ) -> "PhoneNumber":
        return PhoneNumber(
            number=number,
        )

    def __post_init__(self):
        self._check_number()

    def _check_number(self) -> None:
        if not phonenumbers.is_possible_number(phonenumbers.parse(self.number)):
            raise PhoneNumberIsInvalid(f"{self.number} is not a valid phone number")
