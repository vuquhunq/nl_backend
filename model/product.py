from pydantic import BaseModel, Field

from utils.college import PyObjectId


class ProductCreateRequest(BaseModel):
    _id: PyObjectId = Field(PyObjectId, alias='ProductID')
    product_name: str = Field(None, alias='ProductName')
    sell_cost: str = Field(None, alias='SellCost')
