const ulElement = document.querySelector("ul");
const add_itemElement = document.getElementById("add_item");
add_itemElement.addEventListener("click", function () {
  const newItem = document.createElement("li");
  newItem.textContent = "Item";
  ulElement.appendChild(newItem);
});
