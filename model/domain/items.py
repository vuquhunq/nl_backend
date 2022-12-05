from pydantic import BaseModel, Field

from model.domain import IDModel


class ItemsNameModel(BaseModel):
    item_name: str = Field(None, alias='ItemName')


class OrganizationIDMOdel(BaseModel):
    organization_id: str = Field(
        default_factory=IDModel, alias='OrganizationID')


class SKUCodeModel(BaseModel):
    sku_code: str = Field(None, alias="SKUCode")


class InventoryTypeMode(BaseModel):
    inventory_type: str = Field(None, alias='InventoryType')


class SellPriceModel(BaseModel):
    sell_price: float = Field(None, alias='SellPrice')
