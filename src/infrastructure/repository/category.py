from domain import Category, CategoryID, CategoryRepository
from infrastructure import CRUDSQLAlchemyRepository


class SQLAlchemyCategoryRepository(
    CRUDSQLAlchemyRepository[CategoryID, Category],
    CategoryRepository,
):

    @property
    def entity(self) -> type[Category]:
        return Category
