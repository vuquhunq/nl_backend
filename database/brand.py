from fastapi import HTTPException
from fastapi.responses import JSONResponse

from database import database

collection = database.brand


async def create_brand(brand: dict):
    if await collection.insert_one(brand):
        return JSONResponse('Tạo đơn vị tính thành công')


async def check_exist_brand(org: str, brand: str):
    result = await collection.find_one({"OrganizationID": org, "BrandName": brand})
    if result:
        raise HTTPException(200, 'Đã có thương hiệu này trong hệ thống')
    return


async def get_brand_by_org(org: str):
    result = await collection.find({"OrganizationID": org}).to_list(10)
    if result:
        return JSONResponse(result)
    return JSONResponse([])
