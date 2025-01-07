import uuid
from uuid import UUID

from domain.entities.category import Category
from domain.exception.category.category_name_already_exist import CategoryNameAlreadyExist
from domain.repository.category import CategoryRepository
from domain.service.dto.save_category import SaveCategory


class CategoryService:

    def __init__(
        self,
        category_repository: CategoryRepository,
    ):
        self._category_repository = category_repository

    async def save_category(
        self,
        data: SaveCategory,
    ) -> None:
        category = await self._category_repository.get_by_external_id(
            id_=data.external_id,
        )

        if category:
            category.set_image(
                image=data.image,
            )
            category.set_name(
                name=data.name,
            )
            category.set_description(
                description=data.description,
            )
        if not category:
            if await self._category_repository.category_name_exists(name=data.name):
                raise CategoryNameAlreadyExist(f'Category with name "{data.name}" already exist')

            category = Category(
                id=self.generate_id(),
                name=data.name,
                description=data.description,
                image=data.image,
                external_id=data.external_id,
                products=[],
            )

        await self._category_repository.save(
            entity=category,
        )

    @staticmethod
    def generate_id() -> UUID:
        return uuid.uuid4()
