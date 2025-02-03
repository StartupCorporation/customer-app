from interface.web.routes.category.contracts.output.get_categories import CategoryOutputContract


GET_CATEGORIES_RESPONSES = {
    200: {
        'description': 'Existing categories are listed.',
        'model': list[CategoryOutputContract],
    },
}
