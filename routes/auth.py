from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from database.users import create_user
from model.schemas import auth
from utils.jwt import (ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user,
                       create_access_token, get_password_hash, status,
                       timedelta)

route = APIRouter(tags=['Authentication'], prefix='/auth')

@route.post('/sign-in')
async def sign_in(user: auth.SignInRequest):
  user = await authenticate_user(user)
  if not user:
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Incorrect username or password",
          headers={"WWW-Authenticate": "Bearer"},
      )
  access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
  return access_token

@route.post('/sign-up')
async def sign_up(user: auth.SignUpRequest):
  user.password = get_password_hash(user.password)
  user = jsonable_encoder(user)
  print(user)
  result = await create_user(user)
  if result: 
    return 'Success'
  else:
    raise HTTPException(200, 'Bad Request')