from infrastructure.bus.query.exception.base import QueryBusException


class QueryHandlerDoesNotExist(QueryBusException):

    def __init__(
        self,
        detail: str = "Query handler for the provided query doesn't exist.",
    ):
        super().__init__(detail)
