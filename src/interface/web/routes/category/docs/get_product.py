from interface.web.routes.category.contracts.output.product import ProductOutputContract


GET_PRODUCT_RESPONSES = {
    200: {
        'description': 'Product details are provided.',
        'model': ProductOutputContract,
    },
    404: {
        'description': "Product with provided `id` doesn't exist.",
        'content': {
            'application/json': {
                'example': {
                    'detail': "Product with id '<product id>' is not found.",
                },
            }
        }
    }
}
