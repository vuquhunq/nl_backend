from fastapi import HTTPException
from fastapi.responses import JSONResponse

from database import database

collection = database.employee

async def create_doc(docs: dict):
  if await docs.insert_one(docs):
    return JSONResponse('Thêm thành viên thành công')
  raise HTTPException(400, 'Có lỗi khi thêm nhân viên')


async def delete_items(item_id: str):
    delete_result = await collection.delete_one({"_id": item_id})
    if delete_result.deleted_count == 1:
        return JSONResponse('Xoá thành viên thành công', 200)
    raise HTTPException(
        status_code=404, detail=f"Không tìm thấy nhân viên trong hệ thống")