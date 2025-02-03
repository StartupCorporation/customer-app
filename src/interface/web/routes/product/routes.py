from typing import Annotated

from application.queries.get_products.query import GetProductsQuery
from fastapi import APIRouter, status, Path, Depends
from interface.web.routes.product.contracts.output.get_product_details import ProductDetailsOutputContract
from interface.web.routes.product.contracts.output.get_products import ProductsOutputContract
from interface.web.routes.product.docs.get_product_details import GET_PRODUCT_DETAILS_RESPONSES
from interface.web.routes.product.docs.get_products import GET_PRODUCTS_RESPONSES
from pydantic import UUID4

from application.queries.get_product_details.query import GetProductDetailsQuery
from infrastructure.bus.query.bus import QueryBus
from infrastructure.di.container import Container
from interface.web.dependencies.container import get_di_container


router = APIRouter(
    prefix='/product',
    tags=['Product'],
)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    responses=GET_PRODUCTS_RESPONSES,
)
async def get_products(
    container: Annotated[Container, Depends(get_di_container)],
) -> ProductsOutputContract:
    """
    Returns list with short information about the products.
    """
    return await container[QueryBus].handle(
        message=GetProductsQuery(),
    )


@router.get(
    '/{id}/',
    status_code=status.HTTP_200_OK,
    responses=GET_PRODUCT_DETAILS_RESPONSES,
)
async def get_product_details(
    container: Annotated[Container, Depends(get_di_container)],
    id_: Annotated[UUID4, Path(alias='id', description="The product `id`.")],
) -> ProductDetailsOutputContract:
    """
    Returns detailed information about a product.
    """
    return await container[QueryBus].handle(
        message=GetProductDetailsQuery(
            product_id=id_,
        ),
    )
