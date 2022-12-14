from pydantic import BaseModel, Field


class BrandModel(BaseModel):
    brandName: str = Field(None, alias='BrandName')
