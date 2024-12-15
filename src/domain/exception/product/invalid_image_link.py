from domain.exception.base import DomainException


class InvalidImageLink(DomainException):

    def __init__(
        self,
        detail: str = 'Invalid image link',
    ):
        super().__init__(detail=detail)
