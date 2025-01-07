from domain.exception.base import DomainException


class CategoryNameAlreadyExist(DomainException):

    def __init__(
        self,
        detail: str = "Category name already exist",
    ):
        super().__init__(detail)
