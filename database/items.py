from fastapi import HTTPException

from database import database

colection = database.items


async def get_items_by_org(org: str):
  result = await colection.find({"OrganizationID": org}).to_list()
  if result:
    return result
  else: 
    raise HTTPException(400, 'Org is empty')
    
async def create_items(items: dict):
  await colection.insert_one(items)
  return True