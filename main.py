from UI.ui import UI_Eel
from shops_data.search_logic import SearchLogic
import asyncio
from Database.database import Database


class AppLogic:
    def __init__(self):
        self.DB = Database()
        self.UI = UI_Eel
        self.UI.init()
        self.UI.add_on_search_listener(self.search)
        self.UI.start()

    def search(self, item_name):
        print("Searching")
        data = asyncio.run(SearchLogic.search(item_name))[:10]
        print(data)
        self.UI.set_search_results(data)
        self.DB.save_search_history(data, item_name)

        print("end search")

    def show_history(self):
        print("Showing history")


if __name__ == '__main__':
    app = AppLogic()
