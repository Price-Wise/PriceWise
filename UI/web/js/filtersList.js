// Initialize Eel

function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdownContent");
    dropdownContent.classList.toggle("show");
    return false;
}

document.getElementById('search-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const searchItem = document.getElementById('search_item').value;
    const currency = document.getElementById('currency_type').value;
    const maxPrice = parseFloat(document.getElementById('max_price').value);
    const minPrice = parseFloat(document.getElementById('min_price').value);
    const rating = document.getElementById('rating').value;
    const storeLocation = document.getElementById('store_location').value;

    const isValid = await eel.is_valid(searchItem, currency, maxPrice, minPrice, rating, storeLocation)();
    const resultDiv = document.getElementById('result');
    console.log(isValid);
    if (isValid) {
        resultDiv.textContent = 'The input is valid.';
    } else {
        resultDiv.textContent = 'The input is not valid.';
    }
});
