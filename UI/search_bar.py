import eel

# Set web files folder and optionally specify which file types to check for eel.expose()
eel.init('UI')

# Define a function that will handle the search functionality
@eel.expose
def perform_search(query):
    # Here, you can implement your search logic using the provided query
    # For simplicity, let's just print the query for now
    print(f"Performing search: {query}")

# Start the application
eel.start('web/search_bar/search_bar.html', size=(400, 400))