from datetime import datetime

from domain.entities.product import ProductID
from interface.web.contracts import OutputContract


class ProductOutputContract(OutputContract):
    id: ProductID
    name: str
    description: str
    quantity: int
    characteristic: dict

    comments: list["ProductCommentOutputContract"]


class ProductCommentOutputContract(OutputContract):
    author: str
    content: str
    created_at: datetime
