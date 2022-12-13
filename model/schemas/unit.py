from model.domain import CreateAtModel, Field, IDModel, unit


class RequestCreateUnitModel(IDModel, unit.UnitNameModel, CreateAtModel):
  organizationID: str = Field(None, alias='OrganizationID')

