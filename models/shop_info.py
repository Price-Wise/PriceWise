from models.shop_category import ShopCategory


class ShopInfo:
    def __init__(self, name, website, categories: list[ShopCategory]):
        self.name = name
        self.website = website
        self.categories = categories
