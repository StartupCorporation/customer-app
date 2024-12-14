from fastapi import APIRouter
from starlette import status

from domain.entities.product import ProductID
from interface.web.routes.product.contracts.output.product import ProductOutputContract


router = APIRouter(
    prefix='/product',
    tags=['Product'],
)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
)
async def get_product(
    id_: ProductID,
) -> list[ProductOutputContract]:
    pass
