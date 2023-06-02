import asyncio
from models.item import Item
from shops_data.shop_base import ShopBase
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, Tag
from models.shop_category import ShopCategory
import httpx


class Ebay(ShopBase):
    STORE = "Ebay"

    @property
    def shop_categories(self) -> list[ShopCategory]:
        return [ShopCategory.ALL]

    async def get_items(self, search_item) -> list[Item]:
        url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search_item}&_sacat=0"
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(url)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all(
                'li', class_='s-item')
            return [self.get_item_from_dev(search_item) for search_item in search_items]

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find(
            'div', class_='s-item__title')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find(
            'span', class_='s-item__price')
        price = price_elem.text.strip() if price_elem else 'N/A'

        image_element = search_item.find('img')
        image_url = image_element.get('src', '') if isinstance(
            image_element, Tag) else ''

        link_element = search_item.find('a', class_='s-item__link')
        link = link_element.get('href', '') if isinstance(
            link_element, Tag) else ''

        return Item(title, price, Ebay.STORE, link, image_url, '')


if __name__ == "__main__":
    ebay = Ebay()
    data = asyncio.run(ebay.get_items("Iphone 12"))
    print(ebay.shop_categories)

    print(data)
    print(len(data))
