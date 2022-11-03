from fastapi import APIRouter

from model.domain.auth import LoginRequest, LoginResponse, RegisterRequest

routes = APIRouter(tags=['Auth'], prefix='/auth')


@routes.get('/sign-in', response_model=LoginResponse)
def sign_in(request_data: LoginRequest):
    return request_data


@routes.get('/sign-up')
def sign_up(request_data: RegisterRequest):
    return 'Login'
