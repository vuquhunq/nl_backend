from database import database

collection = database.products


async def create_products(product):
    result = await collection.insert_one(product)
    if result:
        return True
    else:
        return False


async def get_all_product():
    result = await collection.find()
    print(result)
    return result
