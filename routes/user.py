
from fastapi import APIRouter, HTTPException

from database.auth import (check_account_password, create_user,
                           find_user_by_username)
from model.auth import SignUpRequest

routes = APIRouter(tags=['Authentication'], prefix='/auth')


@routes.post('/sign-in', response_model_by_alias=SignUpRequest)
async def sign_in(payload: SignUpRequest):
    response = await check_password(payload.username, payload.password)
    if response:
        return "Success"
    raise HTTPException(400, 'Bad Request')


async def check_password(username, password):
    result = await check_account_password(username, password)
    if result:
        return True
    else:
        return False


@ routes.post('/sign-up', response_model_by_alias=SignUpRequest)
async def sign_up(payload: SignUpRequest):
    user_exist = await check_user_exist(payload)
    if not user_exist:
        response = await create_user(payload.dict())
        print(response)
        if response:
            return 'Create user success'
        raise HTTPException(400, 'Bad Request')
    raise HTTPException(400, 'User exist')


async def check_user_exist(user):
    response = await find_user_by_username(user.username)
    if response:
        return True
    else:
        return False
