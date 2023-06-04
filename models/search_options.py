from typing import Literal
from models.shop_category import ShopCategory


class SearchOptions:
    def __init__(self, **kwargs) -> None:
        min_price = kwargs.get('min_price', 0)
        self.min_price: float = float(min_price) if (
            is_number(min_price)) and float(min_price) > 0 else 0

        max_price = kwargs.get('max_price', 10_000_000)
        self.max_price: float = float(max_price) if (
            is_number(max_price)) else 10_000_000
        if self.max_price < self.min_price:
            self.max_price = self.min_price + 1

        category: ShopCategory = kwargs.get('category', ShopCategory.ALL)
        if isinstance(category, str) and any(category.upper() == member.value for member in ShopCategory):
            self.category = ShopCategory[category.upper()]
        else:
            self.category = ShopCategory.ALL

        stores: list[str] = kwargs.get('stores', ['ALL'])
        self.stores: list[str] = [
            'ALL'] if not stores or stores == ['ALL'] else stores

        self.stores_location: Literal['International', 'Jordan', 'ALL'] = kwargs.get(
            'stores_location', 'ALL')
        if self.stores_location not in ['International', 'Jordan', 'ALL']:
            self.stores_location = 'ALL'

        max_stores_results: int = kwargs.get('max_stores_results', 10)
        self.max_stores_results: int = (
            max_stores_results if (is_number(max_stores_results)) else 10
        )

        max_result_num: int = kwargs.get('max_result_num', 10)
        self.max_result_num: int = (
            max_result_num if (is_number(max_result_num)) else 10
        )


def is_number(string):
    try:
        float(string)
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
