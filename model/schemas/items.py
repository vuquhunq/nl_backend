from model.domain import CreateAtModel, brand, files, items, storage, unit


class RequestCreateItem(items.IDModel, items.ItemsNameModel, items.OrganizationIDMOdel, files.UrlImageModel, items.SKUCodeModel, items.SellPriceModel, items.CostPriceMOdel, storage.QuantiyModel, unit.UnitNameModel, brand.BrandModel, CreateAtModel):
    pass


class ResponseBasicInfoItems(items.IDModel, items.ItemsNameModel, files.UrlImageModel, items.SKUCodeModel, items.SellPriceModel):
    pass
