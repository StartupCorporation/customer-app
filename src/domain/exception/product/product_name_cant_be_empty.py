from domain.exception.base import DomainException


class ProductNameCantBeEmpty(DomainException):

    def __init__(
        self,
        detail: str = "Product name can't be empty",
    ):
        super().__init__(detail=detail)
