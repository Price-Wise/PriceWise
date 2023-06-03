from enum import Enum


class ShopCategory(Enum):
    """
    Enum class for shop categories
    """
    ALL = 'All'
    CLOTHES = 'Clothes'
    SHOES = 'Shoes'
    ACCESSORIES = 'Accessories'
    ELECTRONICS = 'Electronics'
    HOME = 'Home'
    OTHER = 'Other'
