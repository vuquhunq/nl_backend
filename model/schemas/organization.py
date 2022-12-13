from pydantic import BaseModel, Field

from model.domain import CreateAtModel, IDModel, files, organization


class ResposneOrganization(IDModel, organization.OrganizationModel, organization.OrganizationBasicInfo, files.UrlImageModel):
    pass


class RequestCreateOrganization(IDModel, CreateAtModel, organization.OrganizationModel, organization.OwnerOrganizationModel, organization.OrganizationBasicInfo, files.UrlImageModel):
    pass
