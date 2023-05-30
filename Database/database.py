from shops_data.item import Item
import json
import uuid

class Database:
    def __init__(self):
        pass

    def save_search_history(self, list_of_items: list[Item], search_item: str):
        search_arr = []
        search_dic = {}

        # Load existing data (if any)
        try:
            with open("Database/search_history.json", "r") as file:
                search_dic = json.load(file)
        except FileNotFoundError:
            pass  # File does not exist initially, so we start with an empty list

        # Add new data
        for item in list_of_items:
            obj ={
                "title": item.name,
                "price": item.price,
                "store": item.store,
                "link": item.url,
                "image_url": item.imageURL,
                "description": item.description,
                "search_item": search_item
            }
            search_arr.append(obj)
            search_dic[str(uuid.uuid4())] = search_arr

        # Write the updated data to the JSON file
        with open("Database/search_history.json", "w") as file:
            json.dump(search_dic, file, indent=4)


    def get_all_search_history(self):
        try:
            with open("Database/search_history.json", "r") as file:
                search_arr = json.load(file)
        except FileNotFoundError:
            return []

        return search_arr

    def get_history(self,id):
        try:
            with open("Database/search_history.json", "r") as file:
                search_arr = json.load(file)
        except FileNotFoundError:
            return []

        return search_arr[id]

        
if __name__ == "__main__":
        database = Database()
        database.save_search_history([Item("iphone","dx","fx","Emam","gd","gh")],"Iphone 12")
        print(database.get_all_search_history())
        print(database.get_history("e4106c69-7d82-443c-9a32-d95770794020"))
