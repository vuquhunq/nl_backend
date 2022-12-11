from pydantic import BaseModel, Field

from model.domain import IDModel


class ItemsNameModel(BaseModel):
    item_name: str = Field('', alias='ItemName')


class OrganizationIDMOdel(BaseModel):
    organization_id: str = Field(
        default_factory=IDModel, alias='OrganizationID')


class SKUCodeModel(BaseModel):
    sku_code: str = Field('', alias="SKUCode")


class InventoryTypeMode(BaseModel):
    inventory_type: str = Field('', alias='InventoryType')


class SellPriceModel(BaseModel):
    sell_price: float = Field('', alias='SellPrice')


class BarcodeModel(BaseModel):
    SKU: str = Field('', alias='SKU')
    UPC: str = Field('', alias='UPC')
    EAN: str = Field('', alias='EAN')
