class ApplicationException(Exception):

    def __init__(
        self,
        detail: str = "Application exception has been happened.",
    ):
        super().__init__(detail)


class NotFound(ApplicationException):

    def __init__(
        self,
        detail: str = "Not found exception.",
    ):
        super().__init__(detail)
