const headerElement = document.querySelector("header");
const red_header = document.querySelector("#red_header");

red_header.addEventListener("click", function () {
  headerElement.classList.add("red");
});
