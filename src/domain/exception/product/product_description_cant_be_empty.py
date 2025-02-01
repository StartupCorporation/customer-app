from domain.exception.base import DomainException


class ProductDescriptionCantBeEmpty(DomainException):

    def __init__(
        self,
        detail: str = "Product description can't be empty",
    ):
        super().__init__(detail=detail)
