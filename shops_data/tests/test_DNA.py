from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


# with sync_playwright() as p:
#     browser = p.firefox.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://www.dna.jo/products/iphone-13?_pos=1&_sid=b86793705&_ss=r')
#     # page.wait_for_load_state()
#     # page.is_visible('body')
#     html=page.content()
#     # print(html)
#     soup = BeautifulSoup(html, "html.parser")
#     titel = soup.find("h1", class_="product-title")
#     print(titel)

#     # print(soup)




def test_DNA():

    with sync_playwright() as p:
        selector = 'h1.product-title'
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_default_timeout(20000)
        page.goto('https://www.dna.jo/products/iphone-13?_pos=1&_sid=b86793705&_ss=r',timeout=0)
        page.wait_for_selector(selector)
        # html = page.content()
        # soup = BeautifulSoup(html, "html.parser")
        # title = soup.find("h1", class_="product-title")
        
        # print(title.text)








    