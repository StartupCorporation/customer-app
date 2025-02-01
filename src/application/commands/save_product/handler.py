from application.commands.save_product.command import SaveProductCommand
from domain.service.product import ProductService
from infrastructure.bus.command.handler import CommandHandler


class SaveProductCommandHandler(CommandHandler[SaveProductCommand]):

    def __init__(
        self,
        product_service: ProductService,
    ):
        self._product_service = product_service

    async def __call__(
        self,
        command: SaveProductCommand,
    ) -> None:
        await self._product_service.save_product(
            name=command.name,
            description=command.description,
            price=command.price,
            quantity=command.quantity,
            images=command.images,
            external_category_id=command.external_category_id,
            external_id=command.external_id,
        )
