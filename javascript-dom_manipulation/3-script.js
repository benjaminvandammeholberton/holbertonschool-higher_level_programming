const headerElement = document.querySelector("header");
const toggler_header = document.getElementById("toggle_header");

toggler_header.addEventListener("click", function () {
  headerElement.classList.toggle("red");
  headerElement.classList.toggle("green");
});
