from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database.customer import (check_customer_by_email, create_customer,
                               get_all_customer_by_org)
from model.domain.items import OrganizationIDMOdel
from model.schemas import customer
from utils.jwt import get_current_user

routes = APIRouter(tags=['Customer'], prefix='/customers')


@routes.post('/get-customer', response_model=List[customer.RequestCreateCustomerModel])
async def get__customer(orgs: OrganizationIDMOdel):
  res = await get_all_customer_by_org(orgs.organization_id)
  if res:
    return res
  return JSONResponse([])


@routes.post('/create-customer', response_model=customer.RequestCreateCustomerModel)
async def create_customers(customer: customer.RequestCreateCustomerModel):
  await check_customer_by_email(customer.customer_email, customer.business_id)

  customer = jsonable_encoder(customer)
  if await create_customer(customer):
    return JSONResponse('Tạo khách hàng thành công')
