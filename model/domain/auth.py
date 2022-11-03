from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(alias='Username')
    password: str = Field(alias='Password')


class LoginResponse(BaseModel):
    access_token: str = Field(alias='AccessToken', default='asdlfkjas;kldf')


class Profile(BaseModel):
    public_name: str = Field(alias='PublicName')
    date_of_birth: str = Field(alias='DateOfBirth')


class RegisterRequest(BaseModel):
    username: str = Field(alias='Username')
    password: str = Field(alias='Password')
    profile: Profile = Field(alias='Profile')
