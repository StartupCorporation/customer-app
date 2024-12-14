from fastapi import APIRouter, status

from domain import CategoryType
from interface.web.routes.category.contracts.output.category import CategoryOutputContract
from interface.web.routes.category.contracts.output.product import CategoryProductOutputContract


router = APIRouter(
    prefix='/category',
    tags=['Category'],
)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
)
async def get_categories() -> list[CategoryOutputContract]:
    pass


@router.get(
    '/products/',
    status_code=status.HTTP_200_OK,
)
async def get_category_products(
    category_type: CategoryType,
) -> list[CategoryProductOutputContract]:
    pass
