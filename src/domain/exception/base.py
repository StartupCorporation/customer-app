class DomainException(Exception):

    def __init__(
        self,
        detail: str = "Domain exception has occurred.",
    ):
        super().__init__(detail)
