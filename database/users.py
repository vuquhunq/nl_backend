from fastapi import HTTPException

from database import database

collection = database.users


async def get_user_by_username(username: str):
  if (user := await collection.find_one({"Username": username})) is not None:
    return user['Password']

async def create_user(user: dict):
  result = await get_user_by_username(user['Username'])
  if result: 
    raise HTTPException(400, 'User exits')
  else:
    await collection.insert_one(user)
    return True