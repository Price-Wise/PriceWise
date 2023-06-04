// selector
const form = document.getElementById("search-options");
const Button = document.getElementById("s-button");
const Enter_press = document.getElementById("search-input");

const checkAllCheckbox = document.getElementById("check-all-stores");
const checkboxes = document.querySelectorAll('input[name="stores"]');

// Events
Button.addEventListener("click", performSearch);
Enter_press.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        performSearch();
    }
});
checkAllCheckbox.addEventListener("change", function () {
    checkboxes.forEach(function (checkbox) {
        checkbox.checked = checkAllCheckbox.checked;
    });
});
checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener("change", function () {
        if (!this.checked) {
            checkAllCheckbox.checked = false;
        }
    });
});

// functions
function performSearch() {
    console.log(getFormValues());
    const query = document.getElementById("search-input").value;
    const searchOptions = getFormValues();
    eel.on_search(query, searchOptions);
    console.log("Search performed");
}

function getFormValues() {
    const formValues = {};
    const inputs = form.elements;
    for (let i = 0; i < inputs.length; i++) {
        formValues[inputs[i].name] = inputs[i].value;
    }
    const checkboxesStores = form.elements["stores"];
    const stores = [];

    for (let i = 0; i < checkboxesStores.length; i++) {
        if (checkboxesStores[i].checked) {
            stores.push(checkboxesStores[i].value);
        }
    }
    formValues["stores"] = stores;
    return formValues;
}
