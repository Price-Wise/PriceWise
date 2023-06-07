import asyncio
import math
from models.shop_category import ShopCategory
from shops_data.shop_base import ShopBase
from models import Item, SearchOptions
from typing import Optional

from shops_data.alibaba import Alibaba
from shops_data.amazon import Amazon
from shops_data.ammancart import ammancart
from shops_data.DNA import DNA
from shops_data.ebay import Ebay
from shops_data.matjarii import Matjarii
from shops_data.open_sooq import openSooq
from shops_data.shein import shein
from shops_data.smartbuy import Smartbuy


class SearchLogic:
    shops: list[ShopBase] = [Amazon(), ammancart(), DNA(),
                             Ebay(), Matjarii(), openSooq(),  Smartbuy(), shein(), Alibaba()]

    @staticmethod
    async def search(search_item: str, search_options: Optional[SearchOptions] = None) -> list[Item]:
        tasks = []
        # stores
        if search_options is not None:
            print(vars(search_options))
        shops = SearchLogic.shops
        if (search_options):
            if 'ALL' not in search_options.stores and len(search_options.stores) >= 1:
                shops = [
                    shop for shop in SearchLogic.shops if shop.info.name in search_options.stores]

            if search_options.stores_location and search_options.stores_location != 'ALL':
                shops = [
                    shop for shop in shops if shop.info.stores_location == search_options.stores_location]

            if search_options.category:
                shops = [
                    shop for shop in shops if search_options.category in shop.info.categories]
        print(shops)

        for shop in shops:
            try:
                task = asyncio.create_task(
                    shop.get_items(search_item, search_options))
                tasks.append(task)
            except Exception as e:
                print(e)

        list_of_items: list[list[Item]] = await asyncio.gather(*tasks)

        all_items: list[Item] = []
        for items in list_of_items:
            all_items.extend(items)

        return SearchLogic.get_most_relevant_items(all_items, search_item, search_options)

    @staticmethod
    def get_most_relevant_items(items: list[Item], search_item: str, search_options: Optional[SearchOptions] = None) -> list[Item]:
        if search_options is None:
            return items
        max_num = search_options.max_result_num
        return items[:max_num]

    @staticmethod
    def get_shops_info():
        return [shop.info for shop in SearchLogic.shops]


if __name__ == "__main__":
    print("start")
    search_options = SearchOptions()
    search_options.stores = ['Smartbuy']
    data = asyncio.run(SearchLogic.search('iphone', search_options))
    print(data)
    print(len(data))
