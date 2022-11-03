from pydantic import BaseModel, Field


class ProductBasicDetail(BaseModel):
    product_id: str = Field(alias='ProductID')
    product_name: str = Field(alias='ProductName')
    cost_price: float = Field(alias='CostPrice')
