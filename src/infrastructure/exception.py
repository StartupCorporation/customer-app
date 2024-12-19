class InfrastructureException(Exception):

    def __init__(
        self,
        detail: str = "Exception has been happened in the infrastructure layer."
    ):
        super().__init__(detail)
