import asyncio
from models.item import Item
from shops_data.shop_base import ShopBase
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, Tag
from models import ShopCategory, ShopInfo
import httpx


class Smartbuy(ShopBase):
    STORE = "Smartbuy"
    info: ShopInfo = ShopInfo(
        "Smartbuy", "https://smartbuy-me.com/smartbuystore/en/", [ShopCategory.ALL], 'Jordan')

    async def get_items(self, search_item, search_options=None) -> list[Item]:
        url = f"https://smartbuy-me.com/smartbuystore/en/search/?text={search_item}"
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(url)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all('div', class_='product-item')

            return [self.get_item_from_dev(search_item) for search_item in search_items]

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find('a', class_='name view-grid hidden-xs')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find('div', class_="price")
        price = price_elem.text.strip() if price_elem else 'N/A'

        link_element = search_item.find('a', class_='thumb')
        link = link_element.get('href', '') if isinstance(
            link_element, Tag) else ''

        image_element = search_item.find('img')
        image_url = image_element.get('src', '') if isinstance(
            image_element, Tag) else ''

        return Item(title, price, Smartbuy.STORE, link, image_url, '')


if __name__ == "__main__":
    smartbuy = Smartbuy()
    data = asyncio.run(smartbuy.get_items('watch'))

    print(data)
