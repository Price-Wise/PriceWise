from abc import ABC, abstractmethod
from shops_data.item import Item
from shops_data.shop_category import ShopCategory


class ShopBase(ABC):

    @abstractmethod
    async def get_items(self, search_item: str) -> list[Item]:
        pass

    @property
    @abstractmethod
    def shop_categories(self) -> list[ShopCategory]:
        pass
