from application.commands.delete_product.command import DeleteProductCommand
from domain.repository.product import ProductRepository
from infrastructure.bus.command.handler import CommandHandler


class DeleteProductCommandHandler(CommandHandler[DeleteProductCommand]):

    def __init__(
        self,
        product_repository: ProductRepository,
    ):
        self._product_repository = product_repository

    async def __call__(
        self,
        command: DeleteProductCommand,
    ) -> None:
        product = await self._product_repository.get_by_external_id(
            external_id=command.external_id,
        )

        if not product:
            return

        await self._product_repository.delete(
            entity=product,
        )
