import eel
import re

# Initialize Eel with the web folder
eel.init('UI/web')

@eel.expose
def is_valid(search_item, currency, max_price, min_price, rating, store_location):
    
    if search_item is None or search_item.strip() == '':
        return False
    
    valid_currencies = ["JD", "USD", "SR"]
    if currency is not None and currency not in valid_currencies:
        return False

    if max_price is not None and (not isinstance(max_price, float) or max_price < 0):
        return False

    if min_price is not None and (not isinstance(min_price, float) or min_price < 0 or min_price >= max_price):
        return False

    # Validate rating: a number between 0 and 5 with up to one decimal place (e.g. 3.5)

    if rating is not None and not re.match(r'^[1-5](\.\d)?$', rating):
        return False

    if store_location is not None and not re.match(r'^[A-Za-z]+(?:[\s-][A-Za-z]+)*$', store_location):
        return False

    # All input values are valid
    return True

# Start the Price-Wise app
eel.start('filters_list/filters-list.html', size=(800, 600), port=8100)
