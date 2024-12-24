from domain.exception.base import DomainException


class CategoryDescriptionCantBeEmpty(DomainException):

    def __init__(
        self,
        detail: str = "Category description cannot be empty",
    ):
        super().__init__(detail)
