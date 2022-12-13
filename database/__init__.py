import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.0')
database = client.IMS_Thesis
