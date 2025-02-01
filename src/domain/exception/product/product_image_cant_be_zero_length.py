from domain.exception.base import DomainException


class ProductImageCantBeZeroLength(DomainException):

    def __init__(
        self,
        detail: str = "Product image can't be zero-length",
    ):
        super().__init__(detail=detail)
