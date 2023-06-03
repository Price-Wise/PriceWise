import eel
from typing import Callable
from pytest import Item


class UI_Eel:
    on_search_listeners: list[Callable] = []
    on_history_click_listeners: list[Callable] = []
    on_view_history_listeners: list[Callable] = []
    on_state_change_listeners: list[Callable] = []

    _state = 'idle'

    @staticmethod
    def init():
        eel.init('UI/web')

    @staticmethod
    def start():
        eel.start('index.html')

    @staticmethod
    def update_state(state: str):
        UI_Eel._state = state
        eel.set_state(state)  # type: ignore

    @staticmethod
    @eel.expose
    def get_state():
        return UI_Eel._state

    # region update UI

    @staticmethod
    @eel.expose
    def set_search_results(items: list[Item]):
        # make list of item to dict
        items_dict = (
            items
            if items and type(items[0]) == dict
            else [vars(item) for item in items]
        )
        eel.update_items(items_dict)  # type: ignore

    @staticmethod
    @eel.expose
    def set_history(history: list[dict]):
        eel.update_history(history)  # type: ignore

    # endregion

    # region events

    @staticmethod
    @eel.expose
    def on_search(query, search_options=None):
        for listener in UI_Eel.on_search_listeners:
            listener(query, search_options)

    @staticmethod
    def add_on_search_listener(listener):
        UI_Eel.on_search_listeners.append(listener)

    @staticmethod
    @eel.expose
    def on_history_click(id):
        print("on_history_click called with ID:", id)
        for listener in UI_Eel.on_history_click_listeners:
            listener(id)

    @staticmethod
    def add_on_history_click_listener(listener):
        UI_Eel.on_history_click_listeners.append(listener)

    @staticmethod
    @eel.expose
    def on_view_history():
        for listener in UI_Eel.on_view_history_listeners:
            listener()

    @staticmethod
    def add_on_view_history_listener(listener):
        UI_Eel.on_view_history_listeners.append(listener)

    # endregion


if __name__ == '__main__':
    items = [
        {
            "name": "WATCH 1/ TSP-W01 TECNO WATCH 1 BLACK ( BUY ONE GET ONE ...",
            "price": "39 JOD",
            "store": "Smartbuy",
            "url": "/smartbuystore/en/Smart-Tech/Mobile-%26-Tablets/Smart-Mobile/TECNO/WATCH-1-TSP-W01-TECNO-WATCH-1-BLACK-%28-BUY-ONE-GET-ONE-FREE-%29/p/TMO0711ST0015",
            "imageURL": "/smartbuystore/medias/TMO0711ST0015.jpg?context=c21hcnRidXliMmN8aW1hZ2VzfDIwNDc5fGltYWdlL2pwZWd8aW1hZ2VzL2gyYy9oNzIvODg3NjE2NDU0NjU5MC9UTU8wNzExU1QwMDE1LmpwZ3wwY2IwM2Y2NTQ0OGYwN2Q2MTI5ZTg1NDg0ZThlMjIwYmU0ZmIwYmRlNzNiNWU5NGZhYmY2YzVjYzNiODAxZDUy",
            "description": "",
        },
        {
            "name": "TSP-W02TECNO Watch 2 | Type : Smart Watch | Color : Bla...",
            "price": "44 JOD",
            "store": "Smartbuy",
            "url": "https://smartbuy-me.com/smartbuystore/en/Wareable-Accessories/TSP-W02TECNO-Watch-2-%7C-Type-%3A-Smart-Watch-%7C-Color-%3A-Black-%7C-Additional-info-%3A-Smartwatch-%7C-warranty-%3A-1/p/TMO0701ST0112",
            "imageURL": "https://smartbuy-me.com/smartbuystore/medias/TMO0701ST0112.jpg?context=c21hcnRidXliMmN8aW1hZ2VzfDg4MDR8aW1hZ2UvanBlZ3xpbWFnZXMvaDJiL2hjZi84ODc2MTY3NjkyMzE4L1RNTzA3MDFTVDAxMTIuanBnfGRkYmI0OWU4YjI3Y2I5NjhiMzUwNDA2YWQyOGJhZDA3ZGFmYjI4YjM2MTk5YTEwNzJiM2Q4MTQxNTFkMTQ2OGI",
            "description": "",
        },
        {
            "name": "HUAWEI Watch GT 3 SE | Type : Wearable | Color : Black ...",
            "price": "",
            "store": "Smartbuy",
            "url": "https://smartbuy-me.com/smartbuystore/en/Wareable-Accessories/HUAWEI-Watch-GT-3-SE-%7C-Type-%3A-Wearable-%7C-Color-%3A-Black-%7C-Additional-info-%3A-Smart-Watch-%7C-warranty-%3A-One-warranty/p/CAV0711ST0063",
            "imageURL": "https://smartbuy-me.com/smartbuystore/medias/CAV0711ST0063.jpg?context=c21hcnRidXliMmN8aW1hZ2VzfDIxODg3fGltYWdlL2pwZWd8aW1hZ2VzL2hkNi9oNDIvODg2ODQ0ODczMTE2Ni9DQVYwNzExU1QwMDYzLmpwZ3xiM2FjMDU1N2QxM2U2MGM2MzFmOGM0MjI0ODUyNzZkYjAxZmQzZDcxMWM4YjE3ODA1MzgyZTY2ODg2ZDc5Mzlk",
            "description": "",
        },
        {
            "name": "HUAWEI Watch GT 3 SE | Type : Wearable | Color : Grey |...",
            "price": "",
            "store": "Smartbuy",
            "url": "https://smartbuy-me.com/smartbuystore/en/Wareable-Accessories/HUAWEI-Watch-GT-3-SE-%7C-Type-%3A-Wearable-%7C-Color-%3A-Grey-%7C-Additional-info-%3A-Smart-Watch-%7C-warranty-%3A-One-warranty/p/CAV0711ST0064",
            "imageURL": "https://smartbuy-me.com/smartbuystore/medias/CAV0711ST0064.jpg?context=c21hcnRidXliMmN8aW1hZ2VzfDIyMDY0fGltYWdlL2pwZWd8aW1hZ2VzL2g3Zi9oNDIvODg2ODQ0ODc2MzkzNC9DQVYwNzExU1QwMDY0LmpwZ3wxZDMwOWYyYjRlM2U2ODFkOTY1MmJiYTdmYzRkNGIyNzU0Yjk3OWQ3NGM0ZjY0NTVhMmNmMzQ2ODJlZTkxOWMw",
            "description": "",
        },
    ]

    UI_Eel.init()
    UI_Eel.set_search_results(items)
    UI_Eel.add_on_search_listener(lambda query: print("hi from listener 1"))
    UI_Eel.add_on_search_listener(lambda query: print(query))

    UI_Eel.start()
