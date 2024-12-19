from dataclasses import dataclass
from uuid import UUID

from infrastructure.bus.query.message import Query


@dataclass(kw_only=True, slots=True, frozen=True)
class GetProductDetailsQuery(Query):
    product_id: UUID
