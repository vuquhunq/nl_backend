from pydantic import BaseModel, Field

from model.domain import IDModel


class QuantiyModel(BaseModel):
  quantity: int = Field(None, alias='Quantity')