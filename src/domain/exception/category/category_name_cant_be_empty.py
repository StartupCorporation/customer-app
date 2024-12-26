from domain.exception.base import DomainException


class CategoryNameCantBeEmpty(DomainException):

    def __init__(
        self,
        detail: str = "Category name can't be empty",
    ):
        super().__init__(detail)
