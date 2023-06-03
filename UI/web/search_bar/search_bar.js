
function performSearch() {
    var query = document.getElementById("search-input").value;
    eel.perform_search(query);
    console.log("Search performed");
}

// Event handler for search button click
var Button = document.getElementById("s-button")
var Enter_press = document.getElementById("search-input")
console.log(Button)

Button.addEventListener("click",performSearch);

Enter_press.addEventListener("key down", function(e) {
    console.log("keydown")// Event handler for search button click
    if (e.key === 'Enter') {
        performSearch();
    }

});




