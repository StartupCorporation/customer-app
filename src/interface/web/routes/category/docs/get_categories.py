from interface.web.routes.category.contracts.output.category import CategoryOutputContract


GET_CATEGORIES_RESPONSES = {
    200: {
        'description': 'Existing categories are listed.',
        'model': list[CategoryOutputContract],
    },
}
