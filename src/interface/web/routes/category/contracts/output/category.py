from domain import CategoryID, CategoryType
from interface.web.contracts import OutputContract


class CategoryOutputContract(OutputContract):
    id: CategoryID
    name: str
    description: str
    type: CategoryType

