import asyncio
from shops_data.item import Item
from shops_data.shop_base import ShopBase
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, Tag
from shops_data.shop_category import ShopCategory
import httpx


class ammancart(ShopBase):
    STORE = "Ammancart"

    @property
    def shop_categories(self) -> list[ShopCategory]:
        return [ShopCategory.ALL]

    async def get_items(self, search_item) -> list[Item]:
        url = f"https://www.ammancart.com/search?q={search_item}"
        with httpx.Client(timeout=20.0) as client:
            response = client.get(url)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all('li', class_='grid__item')
            return [self.get_item_from_dev(search_item) for search_item in search_items]

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find('h3', class_='card__heading h5')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find(
            'span', class_='price-item price-item--regular')
        price = price_elem.text.strip() if price_elem else 'N/A'

        image_element = search_item.find('img', class_='motion-reduce')
        image_url = image_element.get('src', '') if isinstance(
            image_element, Tag) else ''

        link_element = search_item.find('a', class_='full-unstyled-link')
        link = link_element.get('href', '') if isinstance(
            link_element, Tag) else ''

        return Item(title, price, ammancart.STORE, link, image_url, '')


if __name__ == "__main__":
    amman_cart = ammancart()
    data = asyncio.run(amman_cart.get_items("air frier"))
    print(amman_cart.shop_categories)
    print(data)
    print(len(data))
