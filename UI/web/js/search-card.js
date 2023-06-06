let items = [];
let state = "idle";
let shopsInfo = [];

// update the items
eel.expose(update_items);
function update_items(new_items) {
    console.log(new_items);
    items = new_items;
    displayCards(items);
    graph();
}

eel.expose(set_state);
function set_state(new_status) {
    state = new_status;
}

eel.expose(update_shops_info);
function update_shops_info(new_shops_info) {
    shopsInfo = new_shops_info;
    updateStoresDropdown();
}

// ================================================
// ============== Display the cards ===============
// ================================================
//#region cards

const cardTemplate = `
<div class="col-md-6 col-lg-4 col-xxl-3" style="margin-bottom: 12px;">
<div class="card"
  style="border-top-left-radius: 20px;border-top-right-radius: 20px;border-bottom-right-radius: 20px;border-bottom-left-radius: 20px;box-shadow: 2px 2px 16px 8px rgba(0,0,0,0.1);border-style: none;height: 320px;">
  <div class="card-image"
    style="background: url(&quot;assets/img/Mariana%20Souza%20Reis.jpeg&quot;) center / cover;border-top-left-radius: 20px;border-top-right-radius: 20px;position: relative;height: 148px;">
    <div class="d-flex flex-row justify-content-center align-items-center"
      style="border-radius: 39px;width: 60px;height: 60px;position: absolute;bottom: -31px;right: 10px;">
      <button class="btn btn-primary card-iconBtn" data-bss-hover-animate="pulse" type="button"
        style="border-style: none;background: #42a2f1;width: 60px;height: 60px;border-radius: 39px;box-shadow: 2px 2px 20px -1px #757575;"
        data-bs-toggle="modal" data-bs-target="#modal_image"><i class="fa-sharp fa-solid fa-shop"
          style="color: rgb(255,255,255);font-size: 20px;"></i></button>
      <div class="modal fade" role="dialog" tabindex="-1" id="modal_image-5"
        aria-labelledby="exampleModalLabel" style="margin-top: 16vh;">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h4
                style="font-family: 'Source Sans Pro', sans-serif;font-weight: 700;color: #ffa000;letter-spacing: 1px;">
                Maquiagem Artística</h4><button class="btn-close" type="button" aria-label="Close"
                data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <div class="carousel slide" data-bs-ride="carousel" id="carousel-5">
                <div class="carousel-inner">
                  <div class="carousel-item active"><img class="w-100 d-block"
                      src="assets/img/Mariana%20Souza%20Reis.jpeg" alt="Slide Image"></div>
                  <div class="carousel-item"><img class="w-100 d-block"
                      src="assets/img/pexels-karolina-grabowska-4219614.jpg" alt="Slide Image"></div>
                  <div class="carousel-item"><img class="w-100 d-block" src="assets/img/Tia%20lê.jpg"
                      alt="Slide Image"></div>
                </div>
                <div><a class="carousel-control-prev" href="#carousel-5" role="button"
                    data-bs-slide="prev"><span class="carousel-control-prev-icon"></span><span
                      class="visually-hidden">Previous</span></a><a class="carousel-control-next"
                    href="#carousel-5" role="button" data-bs-slide="next"><span
                      class="carousel-control-next-icon"></span><span
                      class="visually-hidden">Next</span></a></div>
                <ol class="carousel-indicators">
                  <li data-bs-target="#carousel-5" data-bs-slide-to="0" class="active"></li>
                  <li data-bs-target="#carousel-5" data-bs-slide-to="1"></li>
                  <li data-bs-target="#carousel-5" data-bs-slide-to="2"></li>
                </ol>
              </div>
            </div>
            <div class="modal-footer"><button class="btn btn-light" data-bss-hover-animate="pulse"
                type="button"
                style="font-family: 'Source Sans Pro', sans-serif;background: #b86868;color: rgb(255,255,255);border-radius: 25px;margin-bottom: 4px;padding-right: 16px;padding-left: 16px;box-shadow: 2px 2px 12px rgba(117,117,117,0.77);border-style: none;"
                data-bs-dismiss="modal">Fechar</button></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="card-body d-flex flex-column justify-content-between" style="padding-bottom: 20px;">
    <div>
      <h6 class="text-muted d-inline mb-2 card-price" 
        style="color: #757575;font-size: 20px;font-family: 'Source Sans Pro', sans-serif;font-weight: 600;border-bottom-right-radius: 10px;border-top-right-radius: 10px;margin-left: -20px;padding-left: 20px;padding-right: 8px;padding-bottom: 2px;background: #cdcf66;padding-top: 2px;">
        45 $</h6>
      <p class="card-description" style="font-family: 'Source Sans Pro', sans-serif;color: #212121;font-weight: bold;">A artística é
        uma técnica diferena que usamos no nosso dia a dia.</p>
    </div>
  </div>
</div>
</div>`;
// Create a function to generate the card from the template

const amazonIcon = `<i class="fab fa-amazon" style="color: rgb(255,255,255);font-size: 20px;"></i>`;
const ebayIcon = `<i class="fa-brands fa-ebay" style="color: rgb(255,255,255);font-size: 30px;"></i>`;
const aliBabaIcon = `<svg style="color: rgb(255,255,255);font-size: 20px;" fill="#FF6600" xmlns="http://www.w3.org/2000/svg" stroke="#FF6600"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M14.391 16.22c-.963.044-.865-.459-.302-1.234 1.32-1.768 3.82-4.236 3.906-5.982.151-2.283-2.143-3.026-4.501-3.004-1.645.022-3.344.492-4.501.906C5 8.315 2.489 10.576.909 13.076-.768 15.554-.216 17.923 3.322 18c2.716-.109 4.48-.862 6.32-1.802.01 0-5.086 1.453-6.958.383l-.008-.002c-.193-.11-.404-.264-.457-.683-.012-.885 1.46-1.802 2.283-2.097v-1.533a5.374 5.374 0 0 0 1.955.366 5.378 5.378 0 0 0 3.472-1.265c.037.13.056.278.044.447h.371c.048-.394-.172-.706-.172-.706-.333-.529-.915-.52-.915-.52s.315.137.529.466a4.953 4.953 0 0 1-4.665.932l1.21-1.2-.336-.874c2.435-.852 4.48-1.507 7.812-2.085l-.746-.624.389-.24c2.01.568 3.325.985 3.253 2.051a2.672 2.672 0 0 1-.202.611c-.584 1.158-2.326 3.09-3.029 3.898-.465.535-.92 1.06-1.245 1.562-.335.503-.54.971-.551 1.42.043 3.504 10.334-1.64 12.324-3.003-2.943 1.266-6.113 2.489-9.609 2.718z"></path></g></svg>`;
const matjariiIcon =
    '<img src="./js/logos/OpenSooq-Logo.png" style="width: 30px; height: 30px; margin-left: 5px; margin-top: 5px; margin-bottom: 5px; margin-right: 5px;"/>';
const openSoqeIcon = `<img src="./js/logos/vertical-logo.png" style="width: 30px; height: 30px; margin-left: 5px; margin-top: 5px; margin-bottom: 5px; margin-right: 5px;"/>'`;
const dnaIcon =
    '<img src="./js/logos/DNA-removebg-preview.png" style="width: 30px; height: 30px; margin-left: 5px; margin-top: 5px; margin-bottom: 5px; margin-right: 5px;"/>';
const smartBuyIcon =
    '<img src="./js/logos/smartbuy.png" style="width: 40px; height: 50px; margin-bottom: 5px; margin-right: 5px;"/>';
const ammanCartIcon =
    '<img src="./js/logos/favicon.webp" style="width: 30px; height: 30px; margin-left: 5px; margin-top: 5px; margin-bottom: 5px; margin-right: 5px;"/>';
const sheInIcon = '<img src="./js/logos/shein-logo-0.png" style="width: 40px; height: 50px"/>';

function generateCard(item) {
    // Create a container element
    const container = document.createElement("div");
    container.innerHTML = cardTemplate.trim();

    // Modify the elements in the container
    const card = container.firstChild;
    const imageDiv = card.querySelector(".card-image");
    imageDiv.style.background = `url('${item.imageURL}') center / contain no-repeat`;

    const priceElement = card.querySelector(".card-price");
    priceElement.textContent = item.price_in_usd + " $";

    const descriptionElement = card.querySelector(".card-description");
    const maxLength = 40; // Maximum length of the description
    const truncatedName =
        item.name.length > maxLength ? item.name.substring(0, maxLength) + "..." : item.name;
    descriptionElement.textContent = truncatedName;

    // Add click event listener to show full description
    descriptionElement.addEventListener("click", function () {
        if (descriptionElement.textContent === truncatedName) {
            descriptionElement.textContent = item.name;
        } else {
            descriptionElement.textContent = truncatedName;
        }
    });

    const iconBtn = card.querySelector(".card-iconBtn");

    if (item.store.toLowerCase() === "amazon") {
        iconBtn.innerHTML = amazonIcon;
    } else if (item.store.toLowerCase() === "ebay") {
        iconBtn.innerHTML = ebayIcon;
    } else if (item.store.toLowerCase() === "alibaba") {
        iconBtn.innerHTML = aliBabaIcon;
    } else if (item.store.toLowerCase() === "matjarii") {
        iconBtn.innerHTML = matjariiIcon;
    } else if (item.store.toLowerCase() === "open sooq") {
        iconBtn.innerHTML = openSoqeIcon;
    } else if (item.store.toLowerCase() === "dna") {
        iconBtn.innerHTML = dnaIcon;
    } else if (item.store.toLowerCase() === "ammancart") {
        iconBtn.innerHTML = ammanCartIcon;
    } else if (item.store.toLowerCase() === "smartbuy") {
        iconBtn.innerHTML = smartBuyIcon;
    } else if (item.store.toLowerCase() === "shein") {
        iconBtn.innerHTML = sheInIcon;
    }

    // Add a link to the card view details
    const linkElement = card.querySelector(".card-iconBtn");
    linkElement.addEventListener("click", function () {
        window.open(item.url, "_blank");
    });

    const cardBody = card.querySelector(".card-body");
    const viewDetailsElement = document.createElement("div");
    viewDetailsElement.textContent = "View Details";
    viewDetailsElement.className = "view-details";
    cardBody.appendChild(viewDetailsElement);

    // Apply smaller font size
    viewDetailsElement.style.fontSize = "smaller";

    // Add click event listener to open item URL
    viewDetailsElement.addEventListener("click", function () {
        window.open(item.url, "_blank");
    });
    // Apply underline on hover
    viewDetailsElement.addEventListener("mouseover", function () {
        viewDetailsElement.style.textDecoration = "underline";
        viewDetailsElement.style.color = "blue";
    });

    // Remove underline when not hovering
    viewDetailsElement.addEventListener("mouseout", function () {
        viewDetailsElement.style.textDecoration = "none";
    });

    // Return the generated card
    return card;
}

const container = document.getElementById("card-container");

function displayCards(itemsCard) {
    container.innerHTML = "";

    for (const item of itemsCard) {
        const card = generateCard(item);
        container.appendChild(card);
    }
}
//#endregion

// ================================================
// ================  fileting  ====================
// ================================================
//#region fileting
const filteringOption = {
    stores: [],
    allStores: true,
    sort: "def",
    minPrice: null,
    maxPrice: null,
};
const checkboxesStores = [];

const sortElem = document.getElementById("sort-select");
const storesShownElem = document.getElementById("stores-shown");
const minPriceElem = document.getElementById("min-price-filter");
const maxPriceElem = document.getElementById("max-price-filter");
const checkAllCheckbox = document.getElementById("check-all-stores-filter");
const storesDropdownMenuFilter = document.getElementById("stores-dropdown-menu-filter");

// Events
checkAllCheckbox.addEventListener("change", function () {
    checkboxesStores.forEach(function (checkbox) {
        checkbox.checked = checkAllCheckbox.checked;
    });
    filteringOption.allStores = checkAllCheckbox.checked;
    filteringOption.stores = [...checkboxesStores]
        .filter((checkbox) => checkbox.checked)
        .map((checkbox) => checkbox.value);
    filter();
});

sortElem.addEventListener("change", (event) => {
    filteringOption.sort = event.target.value;
    filter();
});

minPriceElem.addEventListener("change", (event) => {
    filteringOption.minPrice = event.target.value;
    filter();
});

maxPriceElem.addEventListener("change", (event) => {
    filteringOption.maxPrice = event.target.value;
    filter();
});

//
function updateStoresDropdown() {
    for (const store of shopsInfo) {
        const container = document.createElement("div");
        container.classList.add("form-check");
        container.style.paddingLeft = "31px";

        const input = document.createElement("input");
        container.appendChild(input);
        input.classList.add("form-check-input");
        input.type = "checkbox";
        input.id = "formCheck-" + store.name;
        input.name = "stores-filter";
        input.value = store.name;
        input.checked = true;
        input.addEventListener("change", checkAllStoresFilter);
        checkboxesStores.push(input);

        const label = document.createElement("label");
        container.appendChild(label);
        label.classList.add("form-check-label");
        label.htmlFor = "formCheck-" + store.name;
        label.textContent = store.name;

        storesDropdownMenuFilter.appendChild(container);
    }
}
// Functions
function filter() {
    let filteredItems = [...items];
    console.log(filteringOption);
    if (filteringOption.sort === "lth") {
        filteredItems = filteredItems.sort((a, b) => a.price_in_usd - b.price_in_usd);
    } else if (filteringOption.sort === "htl") {
        filteredItems = filteredItems.sort((a, b) => b.price_in_usd - a.price_in_usd);
    }

    if (filteringOption.allStores === false) {
        filteredItems = filteredItems.filter((item) => {
            return filteringOption.stores.includes(item.store);
        });
    }

    if (filteringOption.minPrice) {
        filteredItems = filteredItems.filter(
            (item) => item.price_in_usd >= filteringOption.minPrice
        );
    }

    if (filteringOption.maxPrice) {
        filteredItems = filteredItems.filter(
            (item) => item.price_in_usd <= filteringOption.maxPrice
        );
    }

    displayCards(filteredItems);
}

function checkAllStoresFilter() {
    if (!this.checked) {
        checkAllCheckbox.checked = false;
    }
    filteringOption.allStores = checkAllCheckbox.checked;
    filteringOption.stores = [...checkboxesStores]
        .filter((checkbox) => checkbox.checked)
        .map((checkbox) => checkbox.value);

    filter();
}
//#endregion

// ================================================
// ==================  Graph  =====================
// ================================================
//#region Graph
function graph() {
    var prices = [];

    for (var i = 0; i < items.length; i++) {
        var priceInUSD = items[i].price_in_usd;

        if (priceInUSD !== null) {
            prices.push(priceInUSD);
        }
    }

    var chartData = {};

    if (prices.length === 0 || prices.every((price) => price === null)) {
        // Handle the case when prices are empty or all values are null (e.g., set empty data for the chart)
        console.log("Prices are empty or all values are null.");
        chartData = {
            labels: ["Min", "Max", "Average"],
            datasets: [
                {
                    label: "Product Price",
                    data: [],
                    backgroundColor: [],
                    borderColor: [],
                    borderWidth: 0,
                },
            ],
        };
    } else {
        var minValue = Math.min(...prices);
        console.log(minValue);
        var maxValue = Math.max(...prices);
        console.log(maxValue);
        var meanValue = prices.reduce((acc, curr) => acc + curr, 0) / prices.length;
        console.log(meanValue);

        chartData = {
            labels: ["Min", "Max", "Average"],
            datasets: [
                {
                    label: "Product Price",
                    data: [minValue, maxValue, meanValue],
                    backgroundColor: [
                        "rgba(255, 0, 0, 1)",
                        "rgba(0, 0, 255, 1)",
                        "rgba(255, 165, 0, 1)",
                    ],
                    lineTension: 0.4,
                    pointRadius: 6,
                    borderColor: "rgba(0, 0, 255, 0.5)", // "rgba(255, 99, 132, 1)
                    borderWidth: 1,
                },
            ],
        };
    }

    var chartOptions = {
        responsive: true,
        maintainAspectRatio: true,
        scales: {
            x: {
                display: prices.length > 0 && !prices.every((price) => price === null), // Show x-axis only if there are non-null prices
            },
            y: {
                beginAtZero: true,
            },
        },
    };

    var chartElement = document.getElementById("barChart");
    var existingChart = Chart.getChart(chartElement);

    if (existingChart) {
        existingChart.destroy(); // Destroy the existing chart if it exists
    }

    new Chart(chartElement, {
        type: "line",
        data: chartData,
        options: chartOptions,
    });
}
//#endregion
