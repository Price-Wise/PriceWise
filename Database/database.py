import datetime
from models import Item
import json
import uuid


class Database:
    def __init__(self):
        pass

    def save_search_history(self, list_of_items: list[Item], search_item: str):
        all_search_result = []

        # Load existing data (if any)
        try:
            with open("Database/search_history.json", "r") as file:
                all_search_result = json.load(file)
        except FileNotFoundError:
            pass  # File does not exist initially, so we start with an empty list

        # Add new data
        search_arr = []
        for item in list_of_items:
            obj = vars(item)
            search_arr.append(obj)

        search_result = {
            "id": str(uuid.uuid4()),
            "search_item": search_item,
            "result": search_arr,
            "date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }

        all_search_result.append(search_result)

        # Write the updated data to the JSON file
        with open("Database/search_history.json", "w") as file:
            json.dump(all_search_result, file, indent=4)

    def get_all_search_history(self):
        try:
            with open("Database/search_history.json", "r") as file:
                search_arr = json.load(file)
        except FileNotFoundError:
            return []

        return search_arr

    def get_history(self, id):
        try:
            with open("Database/search_history.json", "r") as file:
                search_arr: dict = json.load(file)
        except FileNotFoundError:
            return []

        # find the search result with the given id
        for search_result in search_arr:
            if search_result["id"] == id:
                return search_result.get('result', [])

        else:
            return []

    def delete_all_history(self):
        with open("Database/search_history.json", "w") as file:
            json.dump([], file, indent=4)

    def delete_history(self, id):
        try:
            with open("Database/search_history.json", "r") as file:
                search_arr = json.load(file)
        except FileNotFoundError:
            return []

        # find the search result with the given id
        for search_result in search_arr:
            if search_result["id"] == id:
                search_arr.remove(search_result)
                break

        with open("Database/search_history.json", "w") as file:
            json.dump(search_arr, file, indent=4)

    def delete_item(self, history_id, item_id):
        try:
            with open("Database/search_history.json", "r") as file:
                search_arr = json.load(file)
        except FileNotFoundError:
            return []

        # find the search result with the given id
        for search_result in search_arr:
            if search_result["id"] == history_id:
                for item in search_result["result"]:
                    if item["id"] == item_id:
                        search_result["result"].remove(item)
                        break
                break

        with open("Database/search_history.json", "w") as file:
            json.dump(search_arr, file, indent=4)


if __name__ == "__main__":
    database = Database()
    # database.save_search_history(
    #     [Item("iphone", "dx", "fx", "Emam", "gd", "gh"), Item("iphone 2", "dx", "fx", "Emam", "gd", "gh")], "Iphone 12")
    # database.save_search_history([Item("iphone","dx","fx","saif","gd","gh")],"Iphone 13")
    # database.save_search_history([Item("iphone","dx","fx","Emam","gd","gh")],"Iphone 14")
    # database.delete_item("iphone")

    # database.delete_history("80ebed1e-4335-4582-b2b7-52ab85dae5e2")
    # database.delete_item("11ae5947-3ea8-4b88-8c11-8d713674b2e9","79a7777a-ce86-4ad9-803d-e3ac79e59133")
    # database.delete_all_history()
    print(database.get_all_search_history())
    # print(database.get_history("80ebed1e-4335-4582-b2b7-52ab85dae5e2"))
