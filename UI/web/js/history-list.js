search_history = [];

const viewHistoryButton = document.getElementById("view-history-button");
const list = document.getElementById("history-list");

viewHistoryButton.addEventListener("click", () => eel.on_view_history());

eel.expose(update_history);
function update_history(history) {
    search_history = history;
    viewHistory();
}

function viewHistory() {
    console.log("viewHistory");
    list.replaceChildren();
    for (let key of search_history) {
        var newButton = document.createElement("button");
        newButton.textContent = key["search_item"]; // Assign the key as the button text
        newButton.id = key["id"];
        newButton.onclick = function () {
            eel.on_history_click(this.id)();
        };
        list.appendChild(newButton);
    }
}
