from UI.ui import UI_Eel
from shops_data.search_logic import SearchLogic
import asyncio
from Database.database import Database
from typing import Literal


class AppLogic:
    def __init__(self):
        self._state = 'idle'

        self.DB = Database()
        self.UI = UI_Eel
        self.UI.init()
        self.UI.add_on_search_listener(self.search)
        self.UI.add_on_view_history_listener(self.show_all_history)
        self.UI.add_on_history_click_listener(self.show_history)
        self.UI.start()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: Literal['idle', 'searching', 'history']):
        print(f"State changed from {self._state} to {value}")
        self.UI.update_state(value)
        self._state = value

    def search(self, item_name, search_options=None):
        self.state = 'searching'
        # TODO: minimize the number of items
        data = asyncio.run(SearchLogic.search(item_name, search_options))[:10]
        self.UI.set_search_results(data)
        self.DB.save_search_history(data, item_name)
        self.state = 'idle'

    def show_all_history(self):
        print("Showing history")
        self.UI.set_history(self.DB.get_all_search_history())

    def show_history(self, id):
        print("Showing history")
        data = self.DB.get_history(id)
        self.UI.set_search_results(data)


if __name__ == '__main__':
    app = AppLogic()
