from domain.exception.base import DomainException


class PhoneNumberIsInvalid(DomainException):

    def __init__(
        self,
        detail: str = "Phone number is invalid",
    ):
        super().__init__(detail=detail)
