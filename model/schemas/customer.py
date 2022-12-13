from pydantic import Field

from model.domain import IDModel, address, customer, organization


class RequestCreateCustomerModel(IDModel, customer.CustomerNameModel, customer.CustomerEmailModel, address.PhoneNumberModel ):
  business_id: str = Field(None, alias='OrganizationID')
