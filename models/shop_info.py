from models.shop_category import ShopCategory
from typing import Literal


class ShopInfo:
    def __init__(self, name, website, categories: list[ShopCategory], stores_location: Literal['International', 'Jordan']):
        self.name = name
        self.website = website
        self.categories = categories
        self.stores_location = stores_location
