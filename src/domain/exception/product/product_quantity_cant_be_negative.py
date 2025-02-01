from domain.exception.base import DomainException


class ProductQuantityCantBeNegative(DomainException):

    def __init__(
        self,
        detail: str = "Product price can't be negative",
    ):
        super().__init__(detail=detail)
