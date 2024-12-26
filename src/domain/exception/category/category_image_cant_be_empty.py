from domain.exception.base import DomainException


class CategoryImageCantBeEmpty(DomainException):

    def __init__(
        self,
        detail: str = 'Category image can not be empty',
    ):
        super().__init__(detail=detail)
