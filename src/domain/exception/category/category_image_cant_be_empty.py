from domain.exception.base import DomainException


class CategoryImageCantBeZeroLength(DomainException):

    def __init__(
        self,
        detail: str = "Category image can't be zero-length",
    ):
        super().__init__(detail=detail)
