from application.exception.base import NotFound


class ProductNotFoundException(NotFound):

    def __init__(
        self,
        detail: str = "Product isn't found.",
    ):
        super().__init__(detail)
