from application.commands.delete_category.command import DeleteCategoryCommand
from domain.repository.category import CategoryRepository
from infrastructure.bus.command.handler import CommandHandler


class DeleteCategoryCommandHandler(CommandHandler[DeleteCategoryCommand]):

    def __init__(
        self,
        category_repository: CategoryRepository,
    ):
        self._category_repository = category_repository

    async def __call__(
        self,
        command: DeleteCategoryCommand,
    ) -> None:
        category = await self._category_repository.get_by_external_id(
            external_id=command.external_id,
        )

        if not category:
            return

        await self._category_repository.delete(
            entity=category,
        )
