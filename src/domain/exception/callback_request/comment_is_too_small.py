from domain.exception.base import DomainException


class CommentIsTooSmall(DomainException):

    def __init__(
        self,
        detail: str = "The callback request comment is too small",
    ):
        super().__init__(detail=detail)
