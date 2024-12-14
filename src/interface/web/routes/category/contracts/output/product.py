from domain import ProductID
from interface.web.contracts import OutputContract


class CategoryProductOutputContract(OutputContract):
    id: ProductID
    name: str
