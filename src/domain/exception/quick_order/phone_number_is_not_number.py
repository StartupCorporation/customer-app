from domain.exception.base import DomainException


class PhoneNumberIsNotNumberException(DomainException):

    def __init__(
        self,
        detail: str = "Client's phone number must contain only numbers.",
    ):
        super().__init__(detail=detail)
