import asyncio
from shops_data.shop_base import ShopBase
from shops_data.item import Item
from playwright.async_api import async_playwright


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
                             Ebay(), Matjarii(), openSooq(), shein(), Smartbuy()]

    @staticmethod
    async def search(search_item: str) -> list[Item]:
        tasks = []
        for shop in SearchLogic.shops:
            task = asyncio.create_task(shop.get_items(search_item))
            tasks.append(task)

        list_of_items: list[list[Item]] = await asyncio.gather(*tasks)

        all_items = []
        for items in list_of_items:
            all_items.extend(items)

        return all_items


if __name__ == "__main__":
    print("start")
    data = asyncio.run(SearchLogic.search('iphone'))
    print(data)
    print(len(data))
