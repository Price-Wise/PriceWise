import asyncio
from shops_data.item import Item
from shops_data.shop_base import ShopBase
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, Tag
from shops_data.shop_category import ShopCategory
import httpx


class Matjarii(ShopBase):
    STORE = "Matjarii"

    @property
    def shop_categories(self) -> list[ShopCategory]:
        return [ShopCategory.ALL]

    async def get_items(self, search_item) -> list[Item]:
        url = f"https://www.matjarii.com/search?type=product&q={search_item}"
        with httpx.Client(timeout=20.0) as client:
            response = client.get(url)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all(
                'li', class_='item product product-item')
            return [self.get_item_from_dev(search_item) for search_item in search_items]

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find(
            'a', class_='product-item-link')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find(
            'span', class_='price')
        price = price_elem.text.strip() if price_elem else 'N/A'

        image_element = search_item.find('img', class_='product-image-photo')
        image_url = image_element.get('src', '') if isinstance(
            image_element, Tag) else ''

        link_element = search_item.find(
            'a', class_='product photo product-item-photo')
        link = link_element.get('href', '') if isinstance(
            link_element, Tag) else ''

        return Item(title, price, Matjarii.STORE, link, image_url, '')


if __name__ == "__main__":
    matjarii = Matjarii()
    data = asyncio.run(matjarii.get_items("Iphone"))
    print(matjarii.shop_categories)

    print(data)
    print(len(data))
