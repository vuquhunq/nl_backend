from typing import Union

from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

class PasswordModel(BaseModel):
    password: str = Field(None, alias='Password')