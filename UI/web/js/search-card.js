let items = [];
let state = "idle";

// const container = document.getElementById("card-container");

// update the items
eel.expose(update_items);
function update_items(new_items) {
    console.log(new_items);
    items = new_items;
    displayCards();
}

eel.expose(set_state);
function set_state(new_status) {
    console.log(new_status);
    state = new_status;
}

// async function displayCards() {
//     container.replaceChildren();
//     items.forEach((item) => {
//       const cardWrap = document.createElement("div");
//       cardWrap.className = "card-wrap";
//       container.appendChild(cardWrap);

//       const card = document.createElement("div");
//       card.className = "card";
//       cardWrap.appendChild(card);

//       const cardBg = document.createElement("div");
//       cardBg.className = "card-bg";
//       card.appendChild(cardBg);

//       const itemImage = document.createElement("img");
//       itemImage.src = item.imageURL;
//       itemImage.className = "item-image";
//       cardBg.appendChild(itemImage);

//       const cardInfo = document.createElement("div");
//       cardInfo.className = "card-info";
//       cardWrap.appendChild(cardInfo);

//       const itemName = document.createElement("p");
//       itemName.textContent = item.name;
//       itemName.classList.add("item-name");
//       cardInfo.appendChild(itemName);

//       const itemPrice = document.createElement("p");
//       itemPrice.textContent = `Price: ${item.price}`;
//       cardInfo.appendChild(itemPrice);

//       const itemStore = document.createElement("p");
//       itemStore.textContent = `Store: ${item.store}`;
//       cardInfo.appendChild(itemStore);

//       const itemURL = document.createElement("a");
//       itemURL.href = item.url;
//       itemURL.target = "_blank";
//       itemURL.textContent = "View Details";
//       itemURL.className = "item-link"; // Add a class to the link element
//       cardInfo.appendChild(itemURL);
//     });
//   }

//   displayCards();


// Define the card template as a string
const cardTemplate = `
<div class="col-md-6 col-lg-4 col-xxl-3" style="margin-bottom: 12px;">
<div class="card"
  style="border-top-left-radius: 20px;border-top-right-radius: 20px;border-bottom-right-radius: 20px;border-bottom-left-radius: 20px;box-shadow: 2px 2px 16px 8px rgba(0,0,0,0.1);border-style: none;height: 320px;">
  <div class="card-image"
    style="background: url(&quot;assets/img/Mariana%20Souza%20Reis.jpeg&quot;) center / cover;border-top-left-radius: 20px;border-top-right-radius: 20px;position: relative;height: 148px;">
    <div class="d-flex flex-row justify-content-center align-items-center"
      style="border-radius: 39px;width: 60px;height: 60px;position: absolute;bottom: -31px;right: 10px;">
      <button class="btn btn-primary" data-bss-hover-animate="pulse" type="button"
        style="border-style: none;background: #b86868;width: 60px;height: 60px;border-radius: 39px;box-shadow: 2px 2px 20px -1px #757575;"
        data-bs-toggle="modal" data-bs-target="#modal_image"><i class="fab fa-amazon"
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
function generateCard(item) {
    // Create a container element
    const container = document.createElement('div');
    container.innerHTML = cardTemplate.trim();

    // Modify the elements in the container
    const card = container.firstChild;
    const imageDiv = card.querySelector('.card-image');
    imageDiv.style.background = `url('${item.imageURL}') center / contain no-repeat`;

    const priceElement = card.querySelector('.card-price');
    priceElement.textContent = item.price_in_usd + ' $';

    const descriptionElement = card.querySelector('.card-description');
    descriptionElement.textContent = item.name;

    // Return the generated card
    return card;
}

function displayCards() {
    const container = document.getElementById('card-container');
    container.innerHTML = '';

    for (const item of items) {
        const card = generateCard(item);
        container.appendChild(card);
    }
}
// // Example usage:
// const image = 'assets/img/Mariana%20Souza%20Reis.jpeg';
// const price = '45 $';
// const description = 'A artística é uma técnica diferena que usamos no nosso dia a dia.';

// const card = generateCard(image, price, description);
// const container = document.getElementById('card-container');
// container.appendChild(card);











