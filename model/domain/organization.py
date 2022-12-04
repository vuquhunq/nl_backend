from pydantic import BaseModel, Field


class OrganizationModel(BaseModel):
  organization_name: str = Field(None, alias='OrganizationName')

class OwnerOrganizationModel(BaseModel):
  owner: str = Field(None, alias='Owner')