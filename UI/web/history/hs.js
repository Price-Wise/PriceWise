function viewHistory() {
    console.log('viewHistory');
    eel.get_history_from_database()(function(database_history) {
        console.log(database_history);
        var array = [];
        for (var key in database_history) {
            if (database_history.hasOwnProperty(key)) {
                console.log(key + " -> " + database_history[key]);
                array.push(key); // Push the key (ID) into the array
            }
        }
        console.log(array);
        var container = document.querySelector('.container');
        for (var i = 0; i < array.length; i++) {
            var newButton = document.createElement('button');
            newButton.textContent = array[i]; // Assign the key as the button text
            newButton.onclick = function() {
                eel.on_history_click(this.textContent)();
            };
            container.appendChild(newButton);
        }
    });
}
