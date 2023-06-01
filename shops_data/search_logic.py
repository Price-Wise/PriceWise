from shops_data.shop_base import ShopBase
from shops_data.item import Item


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
    shops : list[ShopBase] = [Alibaba(), Amazon(), ammancart(), DNA(), Ebay(), Matjarii(), openSooq(), shein(), Smartbuy()]

    @staticmethod
    def search(search_item: str) -> list[Item]:
        all_items = []

        for shop in SearchLogic.shops:
            all_items.extend(shop.get_items(search_item))

        return all_items

if __name__ == "__main__":
    print(SearchLogic.search('bed cover'))