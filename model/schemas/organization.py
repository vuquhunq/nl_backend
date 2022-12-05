from pydantic import BaseModel, Field

from model.domain import IDModel, files, organization


class ResposneOrganization(IDModel, organization.OrganizationModel, organization.OrganizationBasicInfo, files.UrlImageModel):
    pass


class RequestCreateOrganization(IDModel, organization.OrganizationModel, organization.OwnerOrganizationModel, organization.OrganizationBasicInfo, files.UrlImageModel):
    pass
