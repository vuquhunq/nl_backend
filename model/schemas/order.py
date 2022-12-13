from pydantic import Field

from model.domain import CreateAtModel, IDModel, order


class RequestCreateOrderItems(IDModel, CreateAtModel, order.ListProductModel, order.OrderNameModel):
  organizationID: str = Field(None, alias='OrganizationID')
  customerID: str = Field(None, alias='CustomerID')

class ResponseGetOrderItems(IDModel, CreateAtModel, order.ListProductModel):
  pass
