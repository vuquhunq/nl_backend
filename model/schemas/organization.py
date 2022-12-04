from pydantic import BaseModel, Field

from model.domain import IDModel, organization, users


class ResposneOrganization(IDModel ,organization.OrganizationModel):
  pass
class RequestCreateOrganization(IDModel ,organization.OrganizationModel, organization.OwnerOrganizationModel):
  pass