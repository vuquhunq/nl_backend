
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database.items import create_items, delete_items, get_items_by_org
from model.domain.items import OrganizationIDMOdel
from model.schemas import items

route = APIRouter(tags=['Items'], prefix='/items')


@route.post('/get_item', response_model=List[items.ResponseBasicInfoItems])
async def get_items(orgs: OrganizationIDMOdel):
    res = await get_items_by_org(orgs.organization_id)
    if res:
        return res
    raise HTTPException(404, 'Items not found')


@route.post('/create-item')
async def create_item(item: items.RequestCreateItem):
    item = jsonable_encoder(item)
    resposne = await create_items(item)
    if resposne:
        return JSONResponse('Create items success', 201)
    raise HTTPException(400, 'Bad Request')


@route.delete('/delete-item/')
async def delete_item_by__id(item_id: str):
    res = await delete_items(item_id)
    return res
