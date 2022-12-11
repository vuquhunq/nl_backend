from fastapi import HTTPException
from fastapi.responses import JSONResponse

from database import database

collection = database.users


async def get_user_by_username(username: str):
    if (user := await collection.find_one({"Username": username})) is not None:
        return user['Password']
    else:
        return False


async def create_user(user: dict):
    result = await get_user_by_username(user['Username'])
    if result:
        raise HTTPException(400, 'Tài khoản đã tồn tại')
    res = await collection.insert_one(user)
    if res:
        return JSONResponse('Tạo tài khoản thành công', status_code=201)
