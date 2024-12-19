from infrastructure.exception import InfrastructureException


class DependencyNotFound(InfrastructureException):

    def __init__(
        self,
        detail: str = "Provided dependency is not found.",
    ):
        super().__init__(detail)
