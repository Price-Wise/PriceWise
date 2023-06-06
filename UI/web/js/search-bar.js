function performSearch() {
    var query = document.getElementById("search-input").value;
    showLoadingAnimation(); // Show loading animation
    const searchOptions = getFormValues();
    eel.on_search(
        query,
        searchOptions
    )(function (result) {
        hideLoadingAnimation(); // Hide loading animation
        console.log(result);
        // Process the search result
    });
}

// function performSearch() {
//     console.log(getFormValues());
//     const query = document.getElementById("search-input").value;
//     const searchOptions = getFormValues();
//     eel.on_search(query, searchOptions);
//     console.log("Search performed");
// }

function showLoadingAnimation() {
    var loadingElement = document.getElementById("loading-animation");
    loadingElement.style.display = "flex";
}

function hideLoadingAnimation() {
    var loadingElement = document.getElementById("loading-animation");
    loadingElement.style.display = "none";
}

// Event handler for search button click
const searchButton = document.getElementById("button-addon2");

searchButton.addEventListener("click", function () {
    performSearch();
});

// Event handler for Enter key press
const input = document.getElementById("search-input");
input.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Prevent form submission
        performSearch();
    }
});

// ==============================================
// ============= Search  options ================
// ==============================================
//#region
const formOptions = document.getElementById("search-options");

const checkAllCheckboxOption = document.getElementById("check-all-stores");
const checkboxesOptions = document.querySelectorAll('input[name="stores"]');

console.log(checkboxesOptions);

// Events
checkAllCheckboxOption.addEventListener("change", function () {
    checkboxesOptions.forEach(function (checkbox) {
        checkbox.checked = checkAllCheckboxOption.checked;
    });
});
checkboxesOptions.forEach(function (checkbox) {
    checkbox.addEventListener("change", function () {
        if (!this.checked) {
            checkAllCheckboxOption.checked = false;
        }
    });
});

// functions

function getFormValues() {
    const formValues = {};
    const inputs = formOptions.elements;
    for (let i = 0; i < inputs.length; i++) {
        formValues[inputs[i].name] = inputs[i].value;
    }
    const checkboxesStores = formOptions.elements["stores"];
    const stores = [];

    for (let i = 0; i < checkboxesStores.length; i++) {
        if (checkboxesStores[i].checked) {
            stores.push(checkboxesStores[i].value);
        }
    }
    formValues["stores"] = stores;
    return formValues;
}
//#endregion
