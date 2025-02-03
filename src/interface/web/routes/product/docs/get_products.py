from interface.web.routes.product.contracts.output.get_products import ProductsOutputContract


GET_PRODUCTS_RESPONSES = {
    200: {
        'description': 'Products are listed.',
        'model': ProductsOutputContract,
    },
}
