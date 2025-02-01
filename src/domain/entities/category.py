from dataclasses import dataclass
from uuid import UUID, uuid4

from domain.entities.base import Entity
from domain.exception.category.category_description_cant_be_empty import CategoryDescriptionCantBeEmpty
from domain.exception.category.category_image_cant_be_empty import CategoryImageCantBeZeroLength
from domain.exception.category.category_name_cant_be_empty import CategoryNameCantBeEmpty


@dataclass(kw_only=True)
class Category(Entity[UUID]):
    name: str
    description: str
    image: str
    external_id: UUID

    @classmethod
    def new(
        cls,
        name: str,
        description: str,
        image: str,
        external_id: UUID,
    ) -> "Category":
        return Category(
            id=uuid4(),
            name=name,
            description=description,
            image=image,
            external_id=external_id,
        )

    def __post_init__(self):
        self._check_name(
            name=self.name,
        )
        self._check_description(
            description=self.description,
        )

    def set_description(
        self,
        description: str,
    ) -> None:
        self._check_description(
            description=description,
        )
        self.description = description

    def set_name(
        self,
        name: str,
    ) -> None:
        self._check_name(
            name=name,
        )
        self.name = name

    def set_image(
        self,
        image: str,
    ) -> None:
        self._check_image(
            image=image,
        )
        self.image = image

    @staticmethod
    def _check_image(image: str) -> None:
        if not len(image):
            raise CategoryImageCantBeZeroLength()

    @staticmethod
    def _check_name(name: str) -> None:
        if not name:
            raise CategoryNameCantBeEmpty()

    @staticmethod
    def _check_description(description: str) -> None:
        if not description:
            raise CategoryDescriptionCantBeEmpty()
