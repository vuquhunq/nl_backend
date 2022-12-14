from fastapi import HTTPException
from fastapi.responses import JSONResponse

from database import database

collection = database.customer


async def get_all_customer_by_org(OrganizationID: str):
    result = await collection.find({"OrganizationID": OrganizationID}).to_list(1000)
    if result:
        return result
    else:
        return JSONResponse([])


async def check_customer_by_email(customer: str, org: str):
  if (await collection.find_one({'CustomerEmail': customer, 'OrganizationID': org})) is not None:
    raise HTTPException(409, 'Khách hàng tồn tại')
  return


async def create_customer(customer: dict):
  return await collection.insert_one(customer)

async def delele_customer(customer: str):
    delete_result = await collection.delete_one({"_id": customer})
    if delete_result.deleted_count == 1:
        return JSONResponse('Xóa nhân viên thành công', 200)
    raise HTTPException(
        status_code=404, detail=f"Không tìm thấy nhân viên trong hệ thống")
