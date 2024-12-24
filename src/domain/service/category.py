import uuid
from uuid import UUID

from domain.repository.category import CategoryRepository


class CategoryService:

    def __init__(
        self,
        category_repository: CategoryRepository,
    ):
        self._category_repository = category_repository

    @staticmethod
    def generate_id() -> UUID:
        return uuid.uuid4()
