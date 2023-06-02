let items = [];

// update the items
eel.expose(update_items);
function update_items(new_items) {
    console.log(new_items);
    items = new_items;
    displayCards();
}

async function displayCards() {
    const container = document.getElementById("card-container");

    items.forEach((item) => {
        const cardWrap = document.createElement("div");
        cardWrap.className = "card-wrap";
        container.appendChild(cardWrap);

        const card = document.createElement("div");
        card.className = "card";
        cardWrap.appendChild(card);

        const cardBg = document.createElement("div");
        cardBg.className = "card-bg";
        card.appendChild(cardBg);

        const itemImage = document.createElement("img");
        itemImage.src = item.imageURL;
        itemImage.className = "item-image";
        cardBg.appendChild(itemImage);

        const cardInfo = document.createElement("div");
        cardInfo.className = "card-info";
        cardWrap.appendChild(cardInfo);

        const itemName = document.createElement("p");
        itemName.textContent = item.name;
        itemName.classList.add("item-name");
        cardInfo.appendChild(itemName);

        const itemPrice = document.createElement("p");
        itemPrice.textContent = `Price: ${item.price}`;
        cardInfo.appendChild(itemPrice);

        const itemStore = document.createElement("p");
        itemStore.textContent = `Store: ${item.store}`;
        cardInfo.appendChild(itemStore);

        const itemURL = document.createElement("a");
        itemURL.href = item.url;
        itemURL.target = "_blank";
        itemURL.textContent = "View Details";
        itemURL.className = "item-link"; // Add a class to the link element
        cardInfo.appendChild(itemURL);
    });
}
displayCards();
