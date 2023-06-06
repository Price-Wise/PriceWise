from typing import Literal
from models.shop_category import ShopCategory


class SearchOptions:
    def __init__(self, **kwargs) -> None:
        max_price = kwargs.get('max_price', 10_000_000)
        min_price = kwargs.get('min_price', 0)
        self.max_price = float(max_price) if is_number(
            max_price) else 10_000_000
        self.min_price = float(min_price) if is_number(min_price) else 0
        if self.min_price > self.max_price:
            self.min_price, self.max_price = self.max_price, self.min_price

        category: ShopCategory = kwargs.get('category', '')
        if isinstance(category, str) and any(category == member.value for member in ShopCategory):
            self.category = ShopCategory[category]
        elif isinstance(category, ShopCategory):
            self.category = category
        else:
            self.category = None

        self.stores: list[str] = kwargs.get('stores', ['ALL'])
        if not isinstance(self.stores, list):
            self.stores = ['ALL']

        stores_location: Literal['International', 'Jordan', 'ALL'] = kwargs.get(
            'stores_location', 'ALL')
        if stores_location in ['International', 'Jordan', 'ALL']:
            self.stores_location = stores_location
        else:
            self.stores_location = 'ALL'

        max_stores_results = kwargs.get('max_stores_results', 10)
        self.max_stores_results = int(max_stores_results) if is_number(
            max_stores_results) else 100

        max_result_num = kwargs.get('max_result_num', 10)
        self.max_result_num = int(max_result_num) if is_number(
            max_result_num) else 10000


def is_number(num) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    dict1 = {
        'max_price': 100,
        'min_price': 10,
        'category': 'SHOES',
        'stores': ['Amazon', 'DNA'],
        'stores_location': 'ALL',
        'max_stores_results': 10,
        'max_result_num': 10
    }

    options = SearchOptions()
    options1 = SearchOptions(**dict1)
    print(options.__dict__)
    print(options1.__dict__)
