from application.events.category_saved.event import CategorySavedEvent
from domain.entities.category import Category
from domain.repository.category import CategoryRepository
from domain.service.category import CategoryService
from infrastructure.bus.event.handler import EventHandler


class CategorySavedEventHandler(EventHandler):

    def __init__(
        self,
        category_repository: CategoryRepository,
        category_service: CategoryService,
    ):
        self._category_repository = category_repository
        self._category_service = category_service

    async def __call__(
        self,
        message: CategorySavedEvent,
    ) -> None:
        category = await self._category_repository.get_by_external_id(
            id_=message.external_id,
        )

        if category:
            category.set_image(
                image=message.image,
            )
            category.set_name(
                name=message.name,
            )
            category.set_description(
                description=message.description,
            )
        if not category:
            category = Category(
                id=self._category_service.generate_id(),
                name=message.name,
                description=message.description,
                image=message.image,
                external_id=message.external_id,
                products=[],
            )

        await self._category_repository.save(
            entity=category,
        )
