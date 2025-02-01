from domain.entities.category import Category
from domain.entities.product import Product
from infrastructure.database.relational.models.base import Base
from infrastructure.database.relational.models.product import Product as ProductTable
from infrastructure.database.relational.models.category import Category as CategoryTable


class DatabaseToEntityMapper:

    def __init__(self):
        self._mapping_configuration = {
            Category: {
                "table": CategoryTable.__table__,
            },
            Product: {
                "table": ProductTable.__table__,
            },
        }

    def map(self) -> None:
        mapper_registry = Base.registry

        for entity, mapping_config in self._mapping_configuration.items():
            mapper_registry.map_imperatively(
                class_=entity,
                local_table=mapping_config["table"],
                properties=mapping_config.get("properties"),
            )
