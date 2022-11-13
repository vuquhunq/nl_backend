from fastapi import APIRouter, HTTPException

from database.product import create_products, get_all_product
from model.product import ProductCreateRequest

routes = APIRouter(tags=['Products'], prefix='/products')


@routes.post('/create-product')
async def create_product(product: ProductCreateRequest):
    response = await create_products(product.dict())
    if response:
        return 'Create product Success'
    else:
        return HTTPException(400, 'Create product failure')


@routes.get('/get-product')
async def get_products():
    listProduct = []
    response = get_all_product()
    if response:
        listProduct.append(response)
        return listProduct
    else:
        raise HTTPException(400, 'Bad Request')
