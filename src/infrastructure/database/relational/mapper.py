from sqlalchemy.orm import relationship

from domain.entities.category import Category
from domain.entities.product import Product, Comment
from infrastructure.database.relational.models.base import Base
from infrastructure.database.relational.models.product import Product as ProductTable
from infrastructure.database.relational.models.comment import ProductComment as ProductCommentTable
from infrastructure.database.relational.models.category import Category as CategoryTable


class DatabaseToEntityMapper:

    def __init__(self):
        self._mapping_configuration = {
            Category: {
                "table": CategoryTable.__table__,
                "properties": {
                    # Pay attention to `overlaps` parameter. SQLAlchemy prints a warning
                    #  if this parameter isn't specified
                    "products": relationship(Product, lazy="joined", overlaps="products"),
                },
            },
            Product: {
                "table": ProductTable.__table__,
                "properties": {
                    # Pay attention to `overlaps` parameter. SQLAlchemy prints a warning
                    #  if this parameter isn't specified
                    "comments": relationship(Comment, lazy="joined", overlaps="comments"),
                },
            },
            Comment: {
                "table": ProductCommentTable.__table__,
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
