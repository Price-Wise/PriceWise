form = document.getElementById("search-form");

console.log(form);
form.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log("event");

    query = document.getElementById("search").value;
    eel.on_search(query);
});
