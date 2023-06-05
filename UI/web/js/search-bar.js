function performSearch() {
    var query = document.getElementById("search-input").value;
    eel.on_search(query);
    console.log("Search performed");
}

// Event handler for search button click
var Button = document.getElementById("button-addon2");
var Enter_press = document.getElementById("search-input");
console.log(Button);

Button.addEventListener("click", performSearch);

Enter_press.addEventListener("keydown", function (e) {
    console.log("keydown"); // Event handler for search button click
    if (e.key === "Enter") {
        performSearch();
    }
});
