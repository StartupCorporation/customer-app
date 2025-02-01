from uuid import UUID

from domain.entities.product import Product
from domain.exception.category.category_with_provided_external_id_doesnt_exist import (
    CategoryWithProvidedExternalIdDoesntExist,
)
from domain.repository.category import CategoryRepository
from domain.repository.product import ProductRepository


class ProductService:

    def __init__(
        self,
        category_repository: CategoryRepository,
        product_repository: ProductRepository,
    ):
        self._category_repository = category_repository
        self._product_repository = product_repository

    async def save_product(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        images: list[str],
        external_category_id: UUID,
        external_id: UUID,
    ) -> None:
        category = await self._category_repository.get_by_external_id(
            external_id=external_category_id,
        )

        if not category:
            raise CategoryWithProvidedExternalIdDoesntExist()

        product = await self._product_repository.get_by_external_id(
            external_id=external_id,
        )

        if product:
            product.set_name(
                name=name,
            )
            product.set_description(
                description=description,
            )
            product.set_price(
                price=price,
            )
            product.set_images(
                images=images,
            )
            product.set_quantity(
                quantity=quantity,
            )
        else:
            product = Product.new(
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                images=images,
                category_id=category.id,
                external_id=external_id,
            )

        await self._product_repository.save(
            entity=product,
        )
