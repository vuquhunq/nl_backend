from pydantic import BaseModel, Field

from model.domain import IDModel


class ItemsNameModel(BaseModel):
  item_name: str = Field(None, alias='ItemName')
class OrganizationIDMOdel(BaseModel):
  organization_id: str = Field(default_factory=IDModel, alias='OrganizationID')
