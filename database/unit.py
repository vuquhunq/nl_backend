from fastapi import HTTPException
from fastapi.responses import JSONResponse

from database import database

collection = database.unit

async def create_unit(unit: dict):
  if await collection.insert_one(unit):
    return JSONResponse('Tạo đơn vị tính thành công')

async def check_exist_unit(org: str,unit: str):
  result = await collection.find_one({"OrganizationID": org, "UnitName": unit})
  if result:
    raise HTTPException(200, 'Đã có đơn vị này trong hệ thống')
  return 
                            
async def get_unit_by_org(org: str):
  result = await collection.find({'OrganizationID': org}).to_list(10)
  if result:
    return JSONResponse(result)
  return JSONResponse([])