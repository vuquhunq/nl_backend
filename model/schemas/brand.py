from model.domain import CreateAtModel, Field, IDModel, brand


class RequestCreateBrand(IDModel, brand.BrandModel, CreateAtModel):
  organizationId: str = Field(None, alias="OrganizationID")
