from shops_data.item import Item
from shops_data.shop_base import ShopBase
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup, Tag
from shops_data.shop_category import ShopCategory

class Smartbuy(ShopBase):
    STORE = "Smartbuy"

    @property
    def shop_categories(self) -> list[ShopCategory]:
        return [ShopCategory.ALL]

    def get_items(self, search_item) -> list[Item]:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(
                f"https://smartbuy-me.com/smartbuystore/en/search/?text={search_item}")
            page.wait_for_load_state()
            html = page.content()

            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all('div', class_='product-item')
            print(len(search_items))

            return [self.get_item_from_dev(search_item) for search_item in search_items]

    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find('a', class_='name view-grid hidden-xs')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find('div', class_="price")
        price = price_elem.text.strip() if price_elem else 'N/A'

        link_element = search_item.find('a', class_='thumb')
        link = link_element.get('href', '') if isinstance(link_element, Tag) else ''

        image_element = search_item.find('img')
        image_url = image_element.get('src', '') if isinstance(image_element, Tag) else ''


        return Item(title, price, Smartbuy.STORE, link, image_url,'')
    


if __name__ == "__main__":      
    smartbuy = Smartbuy()
    data = smartbuy.get_items('watch')
    print(smartbuy.shop_categories)

    print(data) 