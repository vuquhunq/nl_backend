from fastapi import HTTPException

from database import database

collection = database.organizations


async def get_organization(username: str):
    response = await collection.find({"Owner": username}).to_list(10)
    if response:
        return response
    return False


async def create_organization_db(_org: dict):
    await collection.insert_one(_org)
    return True


async def check_org_exist(org: str):
    result = await collection.find({"OrganizationName": org}).to_list(10)
    if result:
        raise HTTPException(400, 'Tên tổ chức đã có sẵn trên tài khoản này')
