from shops_data.item import Item
from shops_data.shop_base import ShopBase
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup, Tag
from shops_data.shop_category import ShopCategory

class Alibaba(ShopBase):
    STORE = "Alibaba"

    @property

    def shop_categories(self) -> list[ShopCategory]:    
        return [ShopCategory.ALL]                               
    def get_items(self, search_item) -> list[Item]: 
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(
                # f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={search_item}")
                f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText={search_item}+&viewtype=",timeout=0)
            page.wait_for_load_state()
            html = page.content()

            soup = BeautifulSoup(html, 'html.parser')

            search_items = soup.find_all('div', class_='traffic-product-card')
            print(len(search_items))

            return [self.get_item_from_dev(search_item) for search_item in search_items]
    def get_item_from_dev(self, search_item: Tag) -> Item:
        title_elem = search_item.find('p', class_='elements-title-normal__content')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = search_item.find('span', class_="elements-offer-price-normal__price")
        price = price_elem.text.strip() if price_elem else 'N/A'

        link_element = search_item.find('a', class_='list-no-v2-left__img-container')
        link = link_element.get('href', '') if isinstance(link_element, Tag) else ''

        image_element = search_item.find('div', class_="seb-img-switcher__imgs")
        image_url = image_element.get('data-image', '') if isinstance(image_element, Tag) else ''


        return Item(title, price, Alibaba.STORE, link, image_url,'')
    


if __name__ == "__main__":
    alibaba = Alibaba()
    data = alibaba.get_items('bed cover')
    print(alibaba.shop_categories)

    print(data)



