from pydantic import BaseModel, Field

from model.domain import IDModel


class ItemsNameModel(BaseModel):
    item_name: str = Field('', alias='ItemName')


class OrganizationIDMOdel(BaseModel):
    organization_id: str = Field(
        default_factory=IDModel, alias='OrganizationID')


class SKUCodeModel(BaseModel):
    sku_code: str = Field('', alias="SKUCode")


class SellPriceModel(BaseModel):
    sell_price: float = Field(None, alias='SellPrice')


class CostPriceMOdel(BaseModel):
    cost_price: float = Field(None, alias='CostPrice')
