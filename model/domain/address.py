from pydantic import BaseModel, Field


class AddressStreet(BaseModel):
  street1: str = Field(None, alias='Street1')
  street2: str = Field(None, alias='Street2')
  city: str = Field(None, alias='City')
  state: str = Field(None, alias='State')
  zipcode: str = Field(None, alias='ZipCode')

class PhoneNumberModel(BaseModel):
  phone_number: str = Field(None, alias='PhoneNumber')