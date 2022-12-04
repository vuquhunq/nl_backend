from model.domain import items


class RequestCreateItem(items.IDModel, items.ItemsNameModel, items.OrganizationIDMOdel):
  pass