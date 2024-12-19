from dataclasses import dataclass

from infrastructure.bus.query.message import Query


@dataclass(kw_only=True, slots=True, frozen=True)
class GetCategoriesQuery(Query):
    pass
