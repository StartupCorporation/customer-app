from typing import Annotated

from fastapi import APIRouter, status, Depends

from application.queries.get_categories.query import GetCategoriesQuery
from infrastructure.bus.query.bus import QueryBus
from infrastructure.di.container import Container
from interface.web.dependencies.container import get_di_container
from interface.web.routes.category.contracts.output.get_categories import CategoryOutputContract
from interface.web.routes.category.docs.get_categories import GET_CATEGORIES_RESPONSES


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
    container: Annotated[Container, Depends(get_di_container)],
) -> list[CategoryOutputContract]:
    """
    Returns all categories that exist in the application.
    """
    return await container[QueryBus].handle(
        message=GetCategoriesQuery(),
    )
