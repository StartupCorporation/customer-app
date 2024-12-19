from interface.web.routes.category.contracts.output.category import CategoryProductOutputContract


GET_CATEGORY_PRODUCTS_RESPONSES = {
    200: {
        'description': 'Category products are listed.',
        'model': list[CategoryProductOutputContract],
    },
}
