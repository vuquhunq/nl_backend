
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from database.items import create_items
from model.domain.items import OrganizationIDMOdel
from model.schemas import item

route = APIRouter(tags=['Items'], prefix='/items')

@route.post('/get_item')
async def get_items(orgs: OrganizationIDMOdel):
  orgs = jsonable_encoder(orgs)
  return orgs

@route.post('/create-item')
async def create_item(item: item.RequestCreateItem):
  item = jsonable_encoder(item)
  resposne = await create_items(item)
  if resposne: 
    return 'Success'
  else:
    raise HTTPException(400, 'xui')
