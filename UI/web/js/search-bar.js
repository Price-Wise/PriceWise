let state = "idle";

eel.expose(set_state);
function set_state(new_status) {
    state = new_status;
    console.log(state);
    if (state === "idle") {
        hideLoadingAnimation();
    } else {
        showLoadingAnimation();
    }
}

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
let availableStores = [];

const formOptions = document.getElementById("search-options");

const storesSearchOptions = document.getElementById("stores-search-options");
let checkAllCheckboxOption = document.getElementById("check-all-stores");
const storesExpandBtn = document.getElementById("stores-search-options-expand-btn");
const storeLocationDd = document.getElementById("stores-location-dd");
const categoryDd = document.getElementById("category-dd");
const checkboxesOptions = [];
updateStoresSearchOptions(shopsInfo);

// Events
storesExpandBtn.addEventListener("click", filterStores);
storeLocationDd.addEventListener("change", filterStores);
categoryDd.addEventListener("change", filterStores);
//

function updateStoresSearchOptions(newStores) {
    storesSearchOptions.innerHTML = `
    <div class="form-check store check list" style="font-size: small">
        <input
            class="form-check-input"
            type="checkbox"

            id="check-all-stores"
            value="ALL"
        /><label class="form-check-label" for="check-all-stores"
            >All</label
        >
    </div>`;
    checkAllCheckboxOption = document.getElementById("check-all-stores");
    checkAllCheckboxOption.addEventListener("change", checkAllBtnHandler);

    availableStores = newStores.map((store) => store.name);
    console.log(availableStores);

    for (const store of newStores) {
        const container = document.createElement("div");
        container.classList.add("form-check", "store", "check", "list");
        container.style.fontSize = "small";

        const input = document.createElement("input");
        container.appendChild(input);
        input.classList.add("form-check-input");
        input.type = "checkbox";
        input.id = "formCheck-" + store.name;
        input.value = store.name;
        input.name = "stores";

        const label = document.createElement("label");
        container.appendChild(label);
        label.classList.add("form-check-label");
        label.htmlFor = "formCheck-" + store.name;
        label.innerText = store.name;

        input.addEventListener("change", checkAllStoresHandler);
        checkboxesOptions.push(input);
        storesSearchOptions.appendChild(container);
    }
}
// functions

function getFormValues() {
    const formValues = {};
    const inputs = formOptions.elements;
    for (let i = 0; i < inputs.length; i++) {
        formValues[inputs[i].name] = inputs[i].value;
    }
    const checkboxesStores = formOptions.elements["stores"] || [];
    const stores = [];

    for (let i = 0; i < checkboxesStores.length; i++) {
        if (checkboxesStores[i].checked) {
            stores.push(checkboxesStores[i].value);
        }
    }
    formValues["stores"] = stores;
    return formValues;
}

function filterStores() {
    let stores = shopsInfo;
    const formValues = getFormValues();
    console.log(formValues);

    if (formValues["category"] && formValues["category"] !== "All")
        stores = stores.filter(
            (store) =>
                store.categories.includes(formValues["category"]) ||
                store.categories.includes("GENERAL")
        );

    if (formValues["stores_location"] && formValues["stores_location"] !== "All")
        stores = stores.filter((store) => store.stores_location === formValues["stores_location"]);

    stores = stores.filter((store) => availableStores.includes(store.name));
    updateStoresSearchOptions(stores);
}

function checkAllStoresHandler() {
    if (!this.checked) {
        checkAllCheckboxOption.checked = false;
    }
}

function checkAllBtnHandler() {
    checkboxesOptions.forEach(function (checkbox) {
        checkbox.checked = checkAllCheckboxOption.checked;
    });
}
//#endregion

// ==============================================
// ============= camera  search  ================
// ==============================================
//#region
const searchByCameraBtn = document.getElementById("search-by-camera-btn");

searchByCameraBtn.addEventListener("click", async function () {
    try {
        showLoadingAnimation();
        const searchOptions = getFormValues();
        const result = await eel.on_open_camera(searchOptions)();
    } catch (error) {
        hideLoadingAnimation();
        console.log(error);
    }
});

//#endregion
