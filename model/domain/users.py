from pydantic import BaseModel, EmailStr, Field

from model import ObjectId, PyObjectId
from model.domain import files


class UsernameModel(BaseModel):
  username: str = Field(None, alias='Username')
class EmailModel(BaseModel):
  email: EmailStr = Field(None, alias='Email')


class PublicNameModel(BaseModel):
  public_name: str = Field(None, alias='PublicName')

class AvatarUrl(BaseModel):
  avatart_url: str =Field(default_factory=files.UrlImageModel, alias='AvatarURL')