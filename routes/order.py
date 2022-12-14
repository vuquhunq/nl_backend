from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database.order import create_order, delete_items, get_order_by_org
from model.domain.auth import TokenData
from model.domain.items import OrganizationIDMOdel
from model.schemas import order
from utils.jwt import get_current_user

routes = APIRouter(tags=['Order'], prefix='/order')


@routes.post('/get-order-by-organization', response_model=order.ResponseGetOrderItems)
async def order_by_organization(OrganizationID: OrganizationIDMOdel):
  res = await get_order_by_org(OrganizationID.organization_id)
  if res:
    return res


@routes.post('/create-order-items')
async def create_order_items(order: order.RequestCreateOrderItems, user: TokenData = Depends(get_current_user)):
  order = jsonable_encoder(order)
  result = await create_order(order)
  if result:
    return JSONResponse('Tạo đơn hàng thành công')
  raise HTTPException(400, 'Có lỗi khi tạo đơn hàng')


@routes.delete('/delete-order-item')
async def delele_order_item(id: str):
  res = await delete_items(id)
  return res
