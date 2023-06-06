let search_history = [];

const viewHistoryButton = document.getElementById("search-input");
const list = document.getElementById("searchHistory");

viewHistoryButton.addEventListener("click", () => eel.on_view_history());

eel.expose(update_history);
function update_history(history) {
    search_history = history;
    viewHistory();
}

// Initialize a variable to track the history view state

function viewHistory() {
    console.log("viewHistory");
    list.replaceChildren();

    // <button type="button" class="btn btn-light">Light</button>
        for (let key of search_history) {
            var newButton = document.createElement("button"); // Create a button element for each item
            newButton.textContent = key["search_item"]; // Assign the key as the button text
            newButton.id = key["id"];
            newButton.type = "button";
            newButton.classList.add("btn", "btn-light");
            newButton.onclick = function () {
                eel.on_history_click(this.id)();
            };
            newButton.classList.add("history-button");
            list.appendChild(newButton); // Append the button to the list or desired parent element
        }

        
    }






// clearHistoryButton = document.getElementById("clear-history-button");
// clearHistoryButton.addEventListener("click", () => {eel.on_clear_all_history()

// update_history([])
// });

// eel.expose(clear_history);


    
