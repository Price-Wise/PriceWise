from abc import ABC, abstractmethod
from shops_data.item import Item


class ShopBase(ABC):
    @abstractmethod
    def get_items(self, search_item: str) -> list[Item]:
        pass
