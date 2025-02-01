from domain.exception.base import DomainException


class ProductPriceCantBeLessOrEqualToZero(DomainException):

    def __init__(
        self,
        detail: str = "Product price can't be less or equal to zero",
    ):
        super().__init__(detail=detail)
