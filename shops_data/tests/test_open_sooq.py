import pytest
# from open_sooq import openSooq
# from bs4 import BeautifulSoup
from models.item import Item


def test_get_items_happy_path(self, open_sooq):
    search_item = "خزانة"
    items = open_sooq.get_items(search_item)
    assert isinstance(items, list)
    assert all(isinstance(item, Item) for item in items)


def test_get_items_expected_failure(self, open_sooq):
    search_item = "nonexistent_item"
    items = open_sooq.get_items(search_item)
    assert isinstance(items, list)
    assert len(items) == 0

# def test_get_item_from_dev_edge_case(self, open_sooq):
#     search_item = BeautifulSoup('', 'html.parser').new_tag('div')
#     item = open_sooq.get_item_from_dev(search_item)
#     assert isinstance(item, Item)
#     assert item.title == 'N/A'
#     assert item.price == 'N/A'
#     assert item.store == open_sooq.STORE
#     assert item.link == ''
#     assert item.image_url == ''
#     assert item.additional_info == ''
