from fastapi import HTTPException
from fastapi.responses import JSONResponse

from database import database

collection = database.items


async def get_items_by_org(org: str):
    result = await collection.find({"OrganizationID": org}).to_list(1000)
    if result:
        return result
    else:
        return JSONResponse([])


async def create_items(items: dict):
    result = await collection.insert_one(items)
    if result:
        return True
    raise HTTPException(400, "Lỗi!, Kiểm tra thông tin nhập")


async def delete_items(item_id: str):
    delete_result = await collection.delete_one({"_id": item_id})
    if delete_result.deleted_count == 1:
        return JSONResponse('Xóa sản phẩm thành công', 200)
    raise HTTPException(
        status_code=404, detail=f"Không tìm thấy sản phẩm trong hệ thống")
