from pydantic import UUID4

from infrastructure.bus.query.message import Query


class GetProductDetailsQuery(Query):
    product_id: UUID4
