from interface.web.routes.product.contracts.output.get_product_details import ProductDetailsOutputContract


GET_PRODUCT_DETAILS_RESPONSES = {
    200: {
        'description': 'Product details are provided.',
        'model': ProductDetailsOutputContract,
    },
    404: {
        'description': "Product with provided `id` doesn't exist.",
        'content': {
            'application/json': {
                'example': {
                    'detail': "Product with id '<product id>' is not found.",
                },
            },
        },
    },
}
