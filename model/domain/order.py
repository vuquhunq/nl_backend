from typing import List

from pydantic import BaseModel, Field

from model.schemas import items


class OrderNameModel(BaseModel):
  order_name: str = Field(None, alias='OrderName')

class OrderQuantity(BaseModel):
    order_quantity: str = Field(None, alias='OrderQuantity')

class ListProductModel(BaseModel):
  Items: List[items.ResponseBasicInfoItems]
