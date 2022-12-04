from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from database.organization import create_organization_db, get_organization
from model.domain import users
from model.schemas import organization
from utils.jwt import get_current_user

route = APIRouter(tags=['Organization'], prefix='/organization')

@route.get('/get-organization', response_model=List[organization.ResposneOrganization])
async def get_current_organization(user: str = Depends(get_current_user)):
  result = await get_organization(user.username)
  if result: 
    return result
  raise HTTPException(200, 'Bad Request')

@route.post('/create-organization')
async def create_organization(_organization: organization.RequestCreateOrganization, user: users.UsernameModel = Depends(get_current_user)):
  _organization.owner = user.username
  _organization = jsonable_encoder(_organization)

  result = await create_organization_db(_organization)
  if result:
    return 'Success'
  raise HTTPException(200, 'Bad Request')
