from infrastructure.exception import InfrastructureException


class QueryBusException(InfrastructureException):

    def __init__(
        self,
        detail: str = "Exception has been happened in the query bus.",
    ):
        super().__init__(detail)
