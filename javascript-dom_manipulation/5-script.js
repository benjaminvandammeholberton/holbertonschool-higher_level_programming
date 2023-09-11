const headerElement = document.querySelector("header");
const update_headerElement = document.getElementById("update_header");

update_headerElement.addEventListener("click", function () {
  headerElement.textContent = "New Header!!!";
});
