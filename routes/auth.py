from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database.organization import get_organization
from database.users import create_user
from model.schemas import auth
from utils.jwt import (ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user,
                       create_access_token, get_current_user,
                       get_password_hash, status, timedelta)

route = APIRouter(tags=['Authentication'], prefix='/auth')


@route.post('/sign-in')
async def sign_in(user: auth.SignInRequest):
    check_empty_input(user)
    user.username = user.username.lower()
    user = await authenticate_user(user)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return access_token


def check_empty_input(user: auth.SignInRequest):
    if user.username == '' and user.password == '':
        raise HTTPException(400, 'Chưa điền thông tin đăng nhập')
    if user.username == '':
        raise HTTPException(400, 'Tên đăng nhâp không được để trống')
    if user.password == '':
        raise HTTPException(400, 'Mật khẩu không được để trống')


@route.post('/sign-up')
async def sign_up(user: auth.SignUpRequest):
    user.username = user.username.lower()
    user.password = get_password_hash(user.password)
    user = jsonable_encoder(user)
    await create_user(user)

@route.get('/get-profile/', response_model=auth.ProfileResponse)
async def _get__profile_user(user: str = Depends(get_current_user) ):
    return user