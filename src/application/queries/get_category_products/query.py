from pydantic import UUID4

from infrastructure.bus.impl.query.message import Query


class GetCategoryProductsQuery(Query):
    category_id: UUID4
