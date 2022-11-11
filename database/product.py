from database import database

collection = database.products

async def create_products(product):
  await collection.create_iem()
