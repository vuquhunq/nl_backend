from pydantic import BaseModel, Field


class UnitNameModel(BaseModel):
  unitName: str = Field(None, alias='UnitName')