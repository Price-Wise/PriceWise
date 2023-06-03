from typing import Optional


class SearchOptions:
    def __init__(self, max_price: Optional[float] = None, min_price: Optional[float] = None) -> None:
        self.max_price = max_price
        self.min_price = min_price
