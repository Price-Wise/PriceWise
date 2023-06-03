import asyncio
from models.item import Item
from shops_data.shop_base import ShopBase
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, Tag
from models import ShopCategory, ShopInfo
import httpx
import re


class shein(ShopBase):
    STORE = "SHEIN"
    info: ShopInfo = ShopInfo(
        "SHEIN", "https://ar.shein.com", [ShopCategory.CLOTHES, ShopCategory.ACCESSORIES, ShopCategory.SHOES, ShopCategory.HOME], 'International')

    async def get_items(self, search_item, search_options=None) -> list[Item]:
        url = f"https://ar.shein.com/pdsearch/{search_item}"
        async with async_playwright() as p:
            browser = await p.chromium.launch(timeout=60000)
            page = await browser.new_page()
            await page.route(re.compile(r"\.(jpg|png|svg)$"),
                             lambda route: route.abort())
            await page.goto(url, timeout=30000)
            await page.wait_for_load_state()
            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')
            search_items = soup.find_all(
                'section', class_='S-product-item')
            return [self.get_item_from_dev(search_item) for search_item in search_items]

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find(
            'a', class_='S-product-item__link_jump S-product-item__link')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find(
            'span', class_='normal-price-ctn__sale-price')
        price = price_elem.text.strip() if price_elem else 'N/A'

        image_element = search_item.find('img')
        image_url = image_element.get('data-src', '') if isinstance(
            image_element, Tag) else ''

        link_element = search_item.find(
            'a', class_='S-product-item__link_jump S-product-item__link')
        link = self.info.website + link_element.get('href', '') if isinstance(
            link_element, Tag) else ''

        return Item(title, price, 'JOD', shein.STORE, link, image_url, '')


if __name__ == "__main__":
    she_in = shein()
    data = asyncio.run(she_in.get_items("مكنسة"))
    # print(she_in.shop_categories)
    print(data)
    print(len(data))
