from fastapi import HTTPException
from fastapi.responses import JSONResponse

from database import database
from model.schemas import order

collection = database.order


async def create_order(order: dict):
    result = await collection.insert_one(order)
    if result:
        return True
    raise HTTPException(400, "Lỗi!, Kiểm tra thông tin nhập")


async def get_order_by_org(org: str):
  result = await collection.find({"OrganizationID": org}).to_list(19)
  if result:
    return result
  else:
      return JSONResponse([])


async def delete_items(item_id: str):
    delete_result = await collection.delete_one({"_id": item_id})
    if delete_result.deleted_count == 1:
        return JSONResponse('Xóa đơn đặt hàng thành công', 200)
    raise HTTPException(
        status_code=404, detail=f"Không tìm thấy đơn đặt hàng trong hệ thống")
