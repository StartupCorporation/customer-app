from typing import Annotated

from fastapi import APIRouter, status, Path

from domain.entities.category import CategoryID
from domain.entities.product import ProductID
from interface.web.routes.category.contracts.output.category import (
    CategoryOutputContract,
    CategoryProductOutputContract,
)
from interface.web.routes.category.contracts.output.product import ProductOutputContract


router = APIRouter(
    prefix='/category',
    tags=['Category'],
)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
)
async def get_categories() -> list[CategoryOutputContract]:
    """
    Returns all categories that exist in the application.
    """


@router.get(
    '/{id}/',
    status_code=status.HTTP_200_OK,
)
async def get_category_products(
    id_: Annotated[CategoryID, Path(alias='id')],
) -> list[CategoryProductOutputContract]:
    """
    Returns list with short information about the products from the specific category.
    """


@router.get(
    '/{category_id}/{id}/',
    status_code=status.HTTP_200_OK,
)
async def get_product(
    category_id: CategoryID,
    id_: Annotated[ProductID, Path(alias='id')],
) -> list[ProductOutputContract]:
    """
    Returns detailed information about a product.
    """

