import eel
from typing import Callable


class UI_V1:
    on_search_listener: list[Callable] = []
    on_history_click_listener: list[Callable] = []

    @staticmethod
    def init():
        eel.init('UI/web')

    @staticmethod
    def start():
        eel.start('em/filters-list.html')

    @staticmethod
    def add_on_search_listener(listener):
        UI_V1.on_search_listener.append(listener)

    @staticmethod
    def add_on_history_click_listener(listener):
        UI_V1.on_history_click_listener.append(listener)

    @staticmethod
    @eel.expose
    def on_search(query):
        for listener in UI_V1.on_search_listener:
            listener(query)

    @staticmethod
    @eel.expose
    def on_history_click(id):
        for listener in UI_V1.on_history_click_listener:
            listener(id)


if __name__ == '__main__':
    UI_V1.init()

    def listener(query):
        print("hi from listener 1")

    UI_V1.add_on_search_listener(listener)
    UI_V1.add_on_search_listener(lambda query: print("hi from listener 2"))
    UI_V1.add_on_search_listener(lambda query: print(query))

    UI_V1.start()
