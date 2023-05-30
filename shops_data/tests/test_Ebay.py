import pytest
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from shops_data.ebay import Ebay
from shops_data.item import Item


def test_get_items():
    ebay = Ebay()
    data = ebay.get_items("Iphone 12")
    assert len(data) > 0
    assert isinstance(data[0], Item)

def test_get_item_from_dev():
    ebay = Ebay()
    data = ebay.get_items("Iphone 12")
    assert len(data) > 0
    assert isinstance(data[0], Item)
    assert data[0].name != 'N/A'
    assert data[0].price != 'N/A'
    assert data[0].store == 'Ebay'
    assert data[0].url != ''
    assert data[0].imageURL != ''
    assert data[0].description == ''

