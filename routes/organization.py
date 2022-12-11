from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database.organization import (check_org_exist, create_organization_db,
                                   get_organization)
from model.domain import users
from model.schemas import organization
from utils.jwt import get_current_user

route = APIRouter(tags=['Organization'], prefix='/organizations')


@route.get('/get-organization', response_model=List[organization.ResposneOrganization])
async def get_current_organization(user: str = Depends(get_current_user)):
    result = await get_organization(user.username)
    if result:
        return result
    raise HTTPException(400, 'Bad Request')


@route.post('/create-organization')
async def create_organization(_organization: organization.RequestCreateOrganization, user: users.UsernameModel = Depends(get_current_user)):
    await check_org_exist(_organization.organization_name)
    _organization.owner = user.username
    _organization = jsonable_encoder(_organization)

    result = await create_organization_db(_organization)
    if result:
        return JSONResponse('Tạo tổ chức kho thành công')
