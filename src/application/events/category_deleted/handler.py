from application.events.category_deleted.event import CategoryDeletedEvent
from domain.repository.category import CategoryRepository
from infrastructure.bus.impl.event.handler import EventHandler


class CategoryDeletedEventHandler(EventHandler):

    def __init__(
        self,
        category_repository: CategoryRepository,
    ):
        self._category_repository = category_repository

    async def __call__(
        self,
        message: CategoryDeletedEvent,
    ) -> None:
        category = await self._category_repository.get_by_external_id(
            id_=message.id,
        )

        if not category:
            return

        await self._category_repository.delete(
            entity=category,
        )
