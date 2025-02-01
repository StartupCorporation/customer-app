from domain.exception.base import DomainException


class CategoryWithProvidedExternalIdDoesntExist(DomainException):

    def __init__(
        self,
        detail: str = "Category with provided external id doesn't exist",
    ):
        super().__init__(detail)
