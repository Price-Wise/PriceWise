import eel

# Set up the web interface
eel.init('UI/web')

# Define a function that will be called from the web interface
@eel.expose
def greet(name):
    return f"Hello, {name}!"

# Start the web interface
eel.start('search_card/filters_list.html', size=(400, 300))
      