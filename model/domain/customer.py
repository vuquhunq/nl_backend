from pydantic import BaseModel, Field


class CustomerNameModel(BaseModel):
  customer_name: str = Field(None, alias='CustomerName')


class CustomerEmailModel(BaseModel):
  customer_email: str = Field(None, alias='CustomerEmail')
