from domain.exception.base import DomainException


class ClientNameIsNotAlphabetic(DomainException):

    def __init__(
        self,
        detail: str = 'Client name must be alphabetic',
    ):
        super().__init__(detail=detail)
