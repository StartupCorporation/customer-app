from dataclasses import dataclass
from uuid import UUID, uuid4

from domain.entities.base import Entity
from domain.exception.product.product_description_cant_be_empty import ProductDescriptionCantBeEmpty
from domain.exception.product.product_image_cant_be_zero_length import ProductImageCantBeZeroLength
from domain.exception.product.product_name_cant_be_empty import ProductNameCantBeEmpty
from domain.exception.product.product_price_cant_be_less_or_equal_to_zero import ProductPriceCantBeLessOrEqualToZero
from domain.exception.product.product_quantity_cant_be_negative import ProductQuantityCantBeNegative


@dataclass(kw_only=True)
class Product(Entity[UUID]):
    name: str
    description: str
    price: float
    quantity: int
    images: list[str]
    external_id: UUID
    category_id: UUID

    @classmethod
    def new(
        cls,
        name: str,
        description: str,
        price: float,
        quantity: int,
        images: list[str],
        external_id: UUID,
        category_id: UUID,
    ) -> "Product":
        return Product(
            id=uuid4(),
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            images=images,
            external_id=external_id,
            category_id=category_id,
        )

    def __post_init__(self):
        self._check_name(
            name=self.name,
        )
        self._check_description(
            description=self.description,
        )
        self._check_price(
            price=self.price,
        )
        self._check_quantity(
            quantity=self.quantity,
        )
        self._check_images(
            images=self.images,
        )

    def set_name(
        self,
        name: str,
    ) -> None:
        self._check_name(name)
        self.name = name

    def set_description(
        self,
        description: str,
    ) -> None:
        self._check_description(
            description=description,
        )
        self.description = description

    def set_price(
        self,
        price: float,
    ) -> None:
        self._check_price(
            price=price,
        )
        self.price = price

    def set_quantity(
        self,
        quantity: int,
    ) -> None:
        self._check_quantity(
            quantity=quantity,
        )
        self.quantity = quantity

    def set_images(
        self,
        images: list[str],
    ) -> None:
        self._check_images(
            images=images,
        )
        self.images= images

    @staticmethod
    def _check_images(images: list[str]) -> None:
        if next(filter(lambda image: not len(image), images), None):
            raise ProductImageCantBeZeroLength()

    @staticmethod
    def _check_name(name: str) -> None:
        if not name:
            raise ProductNameCantBeEmpty()

    @staticmethod
    def _check_description(description: str) -> None:
        if not description:
            raise ProductDescriptionCantBeEmpty()

    @staticmethod
    def _check_price(price: float) -> None:
        if price <= 0:
            raise ProductPriceCantBeLessOrEqualToZero()

    @staticmethod
    def _check_quantity(quantity: int) -> None:
        if quantity < 0:
            raise ProductQuantityCantBeNegative()
