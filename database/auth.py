from database import database

collection = database.user


async def create_user(user):
    await collection.insert_one(user)
    return user


async def check_account_password(account):
    print(account)
    result = await collection.find_one({'username': account['username'], 'password': account['password']})
    print(result)
    return result


async def find_user_by_username(username):
    result = await collection.find_one(username)
    print(result)
    return result
