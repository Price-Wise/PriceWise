function performSearch() {
    var query = document.getElementById("search-input").value;
    showLoadingAnimation(); // Show loading animation
    eel.on_search(query)(function(result) {
        hideLoadingAnimation(); // Hide loading animation
        console.log(result);
        // Process the search result
    });
}

function showLoadingAnimation() {
    var loadingElement = document.getElementById("loading-animation");
    loadingElement.style.display = "flex";
}

function hideLoadingAnimation() {
    var loadingElement = document.getElementById("loading-animation");
    loadingElement.style.display = "none";
}

// Event handler for search button click
var searchButton = document.getElementById("button-addon2");

searchButton.addEventListener("click", function() {
    performSearch();
});


// function performSearch() {
//     var query = document.getElementById("search-input").value;
//     eel.on_search(query);
//     console.log("Search performed");
// }

// // Event handler for search button click
// var Button = document.getElementById("button-addon2");
// var Enter_press = document.getElementById("search-input");
// console.log(Button);

// Button.addEventListener("click", performSearch);

// Enter_press.addEventListener("keydown", function (e) {
//     console.log("keydown"); // Event handler for search button click
//     if (e.key === "Enter") {
//         performSearch();
//     }
// });
