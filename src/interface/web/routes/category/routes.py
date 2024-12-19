from typing import Annotated

from fastapi import APIRouter, status, Path, Depends
from pydantic import UUID4

from application.queries.get_catalog_products.query import GetCategoryProductsQuery
from application.queries.get_catalogs.query import GetCategoriesQuery
from application.queries.get_product_details.query import GetProductDetailsQuery
from infrastructure.bus.query.bus import QueryBus
from infrastructure.di.container import Container
from interface.web.dependencies.container import get_di_container
from interface.web.routes.category.contracts.output.category import (
    CategoryOutputContract,
    CategoryProductOutputContract,
)
from interface.web.routes.category.contracts.output.product import ProductOutputContract
from interface.web.routes.category.docs.get_categories import GET_CATEGORIES_RESPONSES
from interface.web.routes.category.docs.get_category_products import GET_CATEGORY_PRODUCTS_RESPONSES
from interface.web.routes.category.docs.get_product import GET_PRODUCT_RESPONSES


router = APIRouter(
    prefix='/category',
    tags=['Category'],
)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    responses=GET_CATEGORIES_RESPONSES,
)
async def get_categories(
    container: Annotated[Container, Depends(get_di_container)]
) -> list[CategoryOutputContract]:
    """
    Returns all categories that exist in the application.
    """
    return await container[QueryBus].handle(
        message=GetCategoriesQuery(),
    )


@router.get(
    '/{id}/products/',
    status_code=status.HTTP_200_OK,
    responses=GET_CATEGORY_PRODUCTS_RESPONSES,
)
async def get_category_products(
    container: Annotated[Container, Depends(get_di_container)],
    id_: Annotated[UUID4, Path(alias='id', description="The category `id`.")],
) -> list[CategoryProductOutputContract]:
    """
    Returns list with short information about the products from the specific category.
    """
    return await container[QueryBus].handle(
        message=GetCategoryProductsQuery(
            category_id=id_,
        ),
    )


@router.get(
    '/{category_id}/products/{id}/',
    status_code=status.HTTP_200_OK,
    responses=GET_PRODUCT_RESPONSES,
)
async def get_product(
    container: Annotated[Container, Depends(get_di_container)],
    category_id: Annotated[UUID4, Path(description="The category `id`.")],
    id_: Annotated[UUID4, Path(alias='id', description="The product `id`.")],
) -> ProductOutputContract:
    """
    Returns detailed information about a product.
    """
    return await container[QueryBus].handle(
        message=GetProductDetailsQuery(
            product_id=id_,
        ),
    )
