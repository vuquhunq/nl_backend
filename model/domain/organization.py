from pydantic import BaseModel, Field


class OrganizationModel(BaseModel):
    organization_name: str = Field(None, alias='OrganizationName')


class OrganizationBasicInfo(BaseModel):
    in_hand: int = Field(default=0, alias='InHand')
    received: int = Field(default=0, alias='ReceivedItem')
    active_items: int = Field(default=0, alias='ActiveItem')
    all_items: int = Field(default=0, alias='AllItems')


class OwnerOrganizationModel(BaseModel):
    owner: str = Field(None, alias='Owner')
