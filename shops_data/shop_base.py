from abc import ABC, abstractmethod
from typing import Optional
from models.item import Item

from models import ShopInfo, SearchOptions


class ShopBase(ABC):

    @abstractmethod
    async def get_items(self, search_item: str, search_options: Optional[SearchOptions] = None) -> list[Item]:
        pass

    @property
    @abstractmethod
    def info(self) -> ShopInfo:
        pass
