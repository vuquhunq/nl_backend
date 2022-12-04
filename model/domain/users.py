from pydantic import BaseModel, EmailStr, Field

from model import ObjectId, PyObjectId


class UsernameModel(BaseModel):
  username: str = Field(None, alias='Username')
class EmailModel(BaseModel):
  email: EmailStr = Field(None, alias='Email')