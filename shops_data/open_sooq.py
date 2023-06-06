import asyncio
from models.item import Item
from shops_data.shop_base import ShopBase
from bs4 import BeautifulSoup, Tag
from models import ShopCategory, ShopInfo
import httpx


class openSooq(ShopBase):
    STORE = "Open Sooq"
    info: ShopInfo = ShopInfo(
        "Open Sooq", "https://jo.opensooq.com", [ShopCategory.GENERAL], 'Jordan')

    async def get_items(self, search_item, search_options=None) -> list[Item]:
        url = f"https://jo.opensooq.com/ar/find?PostSearch[term]={search_item}"
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(url)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all('div', class_='mb-32 relative')
            items = [self.get_item_from_dev(search_item)
                     for search_item in search_items]
            return self.get_most_relevant_items(items, search_item, search_options)

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find(
            'h2', class_='font-20 breakWord overflowHidden')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find(
            'div', class_='postPrice ms-auto bold alignSelfCenter font-19')
        price = price_elem.text.strip() if price_elem else 'N/A'

        image_element = search_item.find('img', class_='width-100 height-100')
        image_url = image_element.get('src', '') if isinstance(
            image_element, Tag) else ''

        link_element = search_item.find(
            'a', class_='flex flexNoWrap p-16 blackColor radius-8 grayHoverBg ripple boxShadow2 relative')
        link = self.info.website + link_element.get('href', '') if isinstance(
            link_element, Tag) else ''

        return Item(title, price, 'JOD', openSooq.STORE, link, image_url, '')


if __name__ == "__main__":
    open_sooq = openSooq()
    data = asyncio.run(open_sooq.get_items("خزانة"))
    print(data)
    print(len(data))
