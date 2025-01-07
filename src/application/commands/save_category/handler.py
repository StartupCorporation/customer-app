from application.commands.save_category.command import SaveCategoryCommand
from domain.service.category import CategoryService
from infrastructure.bus.command.handler import CommandHandler


class SaveCategoryCommandHandler(CommandHandler):

    def __init__(
        self,
        category_service: CategoryService,
    ):
        self._category_service = category_service

    async def __call__(
        self,
        message: SaveCategoryCommand,
    ) -> None:
        await self._category_service.save_category(
            data=message.to_dto(),
        )
