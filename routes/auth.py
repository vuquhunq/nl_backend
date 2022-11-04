from fastapi import APIRouter, HTTPException

from model.domain.auth import LoginRequest, LoginResponse, RegisterRequest

routes = APIRouter(tags=['Auth'], prefix='/auth')


@routes.post('/sign-in', response_model=LoginResponse)
def sign_in(request_data: LoginRequest):
    if verify_password(request_data.username, request_data.password):
        return LoginResponse(AccessToken='aksjhflasdfhalskhjd')
    else:
        raise HTTPException(status_code=404, detail='User not found')


def verify_password(username, password):
    if username == 'user' and password == 'user':
        return True
    return False


@routes.get('/sign-up')
def sign_up(request_data: RegisterRequest):
    return 'Login'
