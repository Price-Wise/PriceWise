from typing import Literal
import re
import uuid


class Item:
    def __init__(self, name, price: str, currency: Literal['USD', 'JOD', 'EUR'], store, url, imageURL, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = self._parse_price(price)
        self.currency = currency
        self.price_in_usd = self._get_price_in_usd()
        self.store = store
        self.url = url
        self.imageURL = imageURL
        self.description = description

    def __str__(self):
        return f"Item(name={self.name}, price={self.price} {self.currency}, store={self.store}, url={self.url}, imageURL={self.imageURL}, description={self.description})"

    def __repr__(self):
        return self.__str__()

    def _get_price_in_usd(self):
        if self.price is None:
            return None
        if self.currency == 'USD':
            return self.price
        elif self.currency == 'JOD':
            return self.price * 1.41
        elif self.currency == 'EUR':
            return self.price * 1.07
        else:
            raise ValueError(f"Unknown currency: {self.currency}")

    def _parse_price(self, price):
        if price in {"N/A", "None", ""}:
            return None
        price = str(price)
        num = re.findall(
            r'[+-]?(\d+([.]\d*)?(e[+-]?\d+)?|[.]\d+(e[+-]?\d+)?)|$', price)[0][0]
        try:
            return float(num)
        except ValueError:
            return None
