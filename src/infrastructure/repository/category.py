from domain.entities.category import CategoryID, Category
from domain.repository.category import CategoryRepository
from infrastructure.repository.base import CRUDSQLAlchemyRepository


class SQLAlchemyCategoryRepository(
    CRUDSQLAlchemyRepository[CategoryID, Category],
    CategoryRepository,
):

    @property
    def entity(self) -> type[Category]:
        return Category
