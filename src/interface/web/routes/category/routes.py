from typing import Annotated

from fastapi import APIRouter, status, Path, Depends

from domain.entities.category import CategoryID
from domain.entities.product import ProductID
from infrastructure.di.container import Container
from interface.web.dependencies.container import get_di_container
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
async def get_categories(
    container: Annotated[Container, Depends(get_di_container)]
) -> list[CategoryOutputContract]:
    """
    Returns all categories that exist in the application.
    """


@router.get(
    '/{id}/products/',
    status_code=status.HTTP_200_OK,
)
async def get_category_products(
    container: Annotated[Container, Depends(get_di_container)],
    id_: Annotated[CategoryID, Path(alias='id')],
) -> list[CategoryProductOutputContract]:
    """
    Returns list with short information about the products from the specific category.
    """


@router.get(
    '/{category_id}/products/{id}/',
    status_code=status.HTTP_200_OK,
)
async def get_product(
    container: Annotated[Container, Depends(get_di_container)],
    category_id: CategoryID,
    id_: Annotated[ProductID, Path(alias='id')],
) -> list[ProductOutputContract]:
    """
    Returns detailed information about a product.
    """
