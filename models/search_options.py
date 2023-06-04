from typing import Literal
from models.shop_category import ShopCategory


class SearchOptions:
    def __init__(self, **kwargs) -> None:
        self.max_price: float = kwargs.get('max_price', 10_000_000)
        self.min_price: float = kwargs.get('min_price', 0)

        category: ShopCategory = kwargs.get('category', ShopCategory.ALL)
        if isinstance(category, str) and any(category == member.value for member in ShopCategory):
            self.category = ShopCategory[category]
        else:
            self.category = ShopCategory.ALL
        self.stores: list[str] = kwargs.get('stores', ['ALL'])
        self.stores_location: Literal['International', 'Jordan', 'ALL'] = kwargs.get(
            'stores_location', 'ALL')
        self.max_stores_results: int = kwargs.get('max_stores_results', 10)
        self.max_result_num: int = kwargs.get('max_result_num', 10)


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
