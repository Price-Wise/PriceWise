import asyncio
from models.item import Item
from shops_data.shop_base import ShopBase
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, Tag
from models import ShopInfo, ShopCategory
import re


class Alibaba(ShopBase):
    STORE = "Alibaba"
    info: ShopInfo = ShopInfo(
        "Alibaba", 'https://www.alibaba.com/', [ShopCategory.ALL], 'International')

    async def get_items(self, search_item, search_options=None) -> list[Item]:
        url = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={search_item}"

        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.route(re.compile(r"\.(jpg|png|svg)$"),
                             lambda route: route.abort())
            await page.goto(url)
            await page.wait_for_load_state()
            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all('div', class_='traffic-product-card')

            return [self.get_item_from_dev(search_item) for search_item in search_items]

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find(
            'p', class_='elements-title-normal__content')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find(
            'span', class_="elements-offer-price-normal__price")
        price = price_elem.text.strip() if price_elem else 'N/A'

        link_element = search_item.find(
            'a', class_='list-no-v2-left__img-container')
        link = link_element.get('href', '') if isinstance(
            link_element, Tag) else ''

        image_element = search_item.find(
            'div', class_="seb-img-switcher__imgs")
        image_url = image_element.get(
            'data-image', '') if isinstance(image_element, Tag) else ''

        return Item(title, price, Alibaba.STORE, link, image_url, '')


if __name__ == "__main__":
    alibaba = Alibaba()
    data = asyncio.run(alibaba.get_items('bed cover'))

    print(data)
