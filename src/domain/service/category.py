from uuid import UUID

from domain.entities.category import Category
from domain.exception.category.category_name_already_exist import CategoryNameAlreadyExist
from domain.repository.category import CategoryRepository


class CategoryService:

    def __init__(
        self,
        category_repository: CategoryRepository,
    ):
        self._category_repository = category_repository

    async def save_category(
        self,
        name: str,
        description: str,
        image: str,
        external_id: UUID,
    ) -> None:
        category = await self._category_repository.get_by_external_id(
            external_id=external_id,
        )

        if not category:
            if await self._category_repository.category_name_exists(name=name):
                raise CategoryNameAlreadyExist(f'Category with name "{name}" already exist')

            category = Category.new(
                name=name,
                description=description,
                image=image,
                external_id=external_id,
            )
        else:
            category.set_description(
                description=description,
            )
            category.set_image(
                image=image,
            )
            if category.name != name:
                if await self._category_repository.category_name_exists(name=name):
                    raise CategoryNameAlreadyExist(f'Category with name "{name}" already exist')

                category.set_name(
                    name=name,
                )

        await self._category_repository.save(
            entity=category,
        )
