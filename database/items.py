from fastapi import HTTPException
from fastapi.responses import JSONResponse

from database import database

collection = database.items


async def get_items_by_org(org: str):
    result = await collection.find({"OrganizationID": org}).to_list(10)
    if result:
        return result
    else:
        raise HTTPException(400, 'Org is empty')


async def create_items(items: dict):
    result = await collection.insert_one(items)
    if result:
        return True
    raise HTTPException(400, "Bad Request")


async def delete_items(item_id: str):
    delete_result = await collection.delete_one({"_id": item_id})
    print(item_id)
    print(delete_result.deleted_count)
    if delete_result.deleted_count == 1:
        return JSONResponse('Delete success', 200)
    raise HTTPException(status_code=404, detail=f"Not found")
