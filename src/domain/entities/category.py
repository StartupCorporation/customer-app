from dataclasses import dataclass
from uuid import UUID

from domain.entities.base import Entity
from domain.entities.product import Product
from domain.exception.category.category_description_cant_be_empty import CategoryDescriptionCantBeEmpty
from domain.exception.category.category_image_cant_be_empty import CategoryImageCantBeEmpty
from domain.exception.category.category_name_cant_be_empty import CategoryNameCantBeEmpty


@dataclass(kw_only=True)
class Category(Entity[UUID]):
    name: str
    description: str
    image: str
    external_id: UUID

    products: list[Product]

    def __post_init__(self):
        self.set_name(
            name=self.name,
        )
        self.set_description(
            description=self.description,
        )
        self.set_image(
            image=self.image,
        )

    def set_description(
        self,
        description: str,
    ) -> None:
        if not description:
            raise CategoryDescriptionCantBeEmpty()

        self.description = description

    def set_name(
        self,
        name: str,
    ) -> None:
        if not name:
            raise CategoryNameCantBeEmpty()

        self.name = name

    def set_image(
        self,
        image: str,
    ) -> None:
        if not image:
            raise CategoryImageCantBeEmpty()

        self.image = image
