from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database.brand import check_exist_brand, create_brand, get_brand_by_org
from model.domain.items import OrganizationIDMOdel
from model.schemas import brand

routes = APIRouter(tags=['Brand'], prefix='/brand')

@routes.post('/create-brand-org')
async def create_brand_org(brand: brand.RequestCreateBrand):
  await check_exist_brand(brand.organizationId,brand.brandName)
  brand = jsonable_encoder(brand)
  result = await create_brand(brand)
  if result:
    return JSONResponse('Tạo thương hiệu thành công')
  return


@routes.post('/get-brand-org', response_model=brand.RequestCreateBrand)
async def get_brand_orgs(OrganizationID: OrganizationIDMOdel):
  return await get_brand_by_org(OrganizationID.organization_id)


  