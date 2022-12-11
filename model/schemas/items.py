from model.domain import files, items


class RequestCreateItem(items.IDModel, items.ItemsNameModel, items.OrganizationIDMOdel, files.UrlImageModel, items.SKUCodeModel, items.InventoryTypeMode, items.SellPriceModel, items.BarcodeModel):
    pass


class ResponseBasicInfoItems(items.IDModel, items.ItemsNameModel, files.UrlImageModel, items.SKUCodeModel, items.InventoryTypeMode, items.SellPriceModel):
    pass
