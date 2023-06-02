import eel
from typing import Callable
from Database.database import Database

eel.init('UI/web')

on_history_click_listener: list[Callable] = []
@eel.expose
def on_history_click(id):
    print("on_history_click called with ID:", id)
    for listener in on_history_click_listener:
      listener(id)

def add_on_history_click_listener(listener):
    on_history_click_listener.append(listener)

@eel.expose
def get_history_from_database():
    get_all_search_history = Database().get_all_search_history()
    return get_all_search_history




if __name__ == '__main__':
    eel.init('UI/web')

    def listener(query):
        print("hi from listener 1")

    add_on_history_click_listener(listener)
    add_on_history_click_listener(lambda query: print("hi from listener 2"))
    add_on_history_click_listener(lambda query: print(query))

    eel.start('history/hs.html')