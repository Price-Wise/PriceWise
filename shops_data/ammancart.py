import asyncio
from models.item import Item
from shops_data.shop_base import ShopBase
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, Tag
from models import ShopCategory, ShopInfo
import httpx


class ammancart(ShopBase):
    STORE = "Ammancart"
    info: ShopInfo = ShopInfo(
        "Ammancart", "https://www.ammancart.com/", [ShopCategory.ALL])

    async def get_items(self, search_item, search_options=None) -> list[Item]:
        url = f"https://www.ammancart.com/search?q={search_item}"
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(url)
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
    print(data)
    print(len(data))
