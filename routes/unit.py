from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database.unit import check_exist_unit, create_unit, get_unit_by_org
from model.domain.items import OrganizationIDMOdel
from model.schemas import unit

routes = APIRouter(tags=['Unit'], prefix='/unit')


@routes.post('/create-unit-by-org')
async def create_unit_org(unit: unit.RequestCreateUnitModel):
  await check_exist_unit(unit.organizationID, unit.unitName)
  unit = jsonable_encoder(unit)
  res = await create_unit(unit)
  if res:
    return JSONResponse('Tạo đơn vị thành công')


@routes.post('/get-unit-org')
async def get_unit_orgs(OrganizationID: OrganizationIDMOdel):
  return await get_unit_by_org(OrganizationID.organization_id)
