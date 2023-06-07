from UI.ui import UI_Eel
from models import SearchOptions
from shops_data.search_logic import SearchLogic
import asyncio
from Database.database import Database
from typing import Literal, Optional
from cam import cam_app
from detect_product import detect


class AppLogic:
    def __init__(self):
        self._state = 'idle'

        self.DB = Database()
        self.UI = UI_Eel
        self.UI.init()
        self.UI.add_on_search_listener(self.search)
        self.UI.add_on_view_history_listener(self.show_all_history)
        self.UI.add_on_history_click_listener(self.show_history)
        self.UI.add_on_clear_all_history_listener(self.DB.delete_all_history)
        self.UI.set_shops_info(SearchLogic.get_shops_info())
        self.UI.add_on_open_camera_listener(self.open_camera)
        self.UI.start()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: Literal['idle', 'searching', 'history', 'camera-open', 'analyzing-image']):
        print(f"State changed from {self._state} to {value}")
        self.UI.update_state(value)
        self._state = value

    def search(self, item_name, search_options: Optional[SearchOptions] = None):
        self.state = 'searching'
        try:
            # TODO: minimize the number of items
            data = asyncio.run(SearchLogic.search(item_name, search_options))
            self.UI.set_search_results(data)
            self.DB.save_search_history(data, item_name)
            self.state = 'idle'
        except Exception as e:
            print(e)
            self.state = 'idle'

    def show_all_history(self):
        print("Showing history")
        self.UI.set_history(self.DB.get_all_search_history())

    def show_history(self, id):
        print("Showing history")
        data = self.DB.get_history(id)
        self.UI.set_search_results(data)

    def open_camera(self, search_options: Optional[SearchOptions] = None):
        self.state = 'camera-open'
        image = cam_app()
        if image is None:
            self.state = 'idle'
            return

        try:
            self.state = 'analyzing-image'
            results = detect(image)
            name = None
            for result in results:
                detection_count = result.boxes.shape[0]

                for i in range(detection_count):
                    cls = int(result.boxes.cls[i].item())
                    name = result.names[cls]
                    print(f"{name}: {result.boxes.conf[i].item()}")

            if name is not None:
                return self.search(name, search_options)

            self.state = 'idle'
        except Exception as e:
            print(e)
            self.state = 'idle'


if __name__ == '__main__':
    app = AppLogic()
