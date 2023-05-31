import asyncio
from shops_data.item import Item
from shops_data.shop_base import ShopBase
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, Tag
from shops_data.shop_category import ShopCategory


class DNA(ShopBase):
    STORE = "DNA"

    @property
    def shop_categories(self) -> list[ShopCategory]:
        return [ShopCategory.ALL]

    async def get_items(self, search_item) -> list[Item]:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(
                f"https://www.dna.jo/search?type=product&q={search_item}", timeout=0)
            await page.wait_for_load_state()
            html = await page.content()

            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all('article', class_='productitem')

            return [self.get_item_from_dev(search_item) for search_item in search_items]

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find(
            'h2', class_='productitem--title')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find('span', class_='money')
        price = price_elem.text.strip() if price_elem else 'N/A'

        image_element = search_item.find(
            'img', class_='productitem--image-alternate')
        image_url = image_element.get('src', '') if isinstance(
            image_element, Tag) else ''

        link_element = title_elem and title_elem.find('a')
        link = link_element.get('href', '') if isinstance(
            link_element, Tag) else ''

        return Item(title, price, DNA.STORE, link, image_url, '')


if __name__ == "__main__":
    dna = DNA()
    data = asyncio.run(dna.get_items("Iphone 12"))
    print(DNA.shop_categories)

    print(data)
