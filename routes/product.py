from fastapi import APIRouter

from data.product import dummy_data
from model.domain.auth import RegisterRequest
from model.domain.product import ProductBasicDetail

routes = APIRouter(tags=['Products'], prefix='/products')


@routes.get('/get-all-products', response_model_by_alias=ProductBasicDetail)
def get_all_products():
    return dummy_data


@routes.get('/sign-up')
def sign_up(request_data: RegisterRequest):
    return request_data
