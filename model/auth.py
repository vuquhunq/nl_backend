from pydantic import BaseModel, Field


class SignUpRequest(BaseModel):
    username: str = Field(None, alias='Username')
    password: str = Field(None, alias='Password')
