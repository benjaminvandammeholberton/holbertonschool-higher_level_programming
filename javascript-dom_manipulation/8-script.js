document.addEventListener("DOMContentLoaded", function () {
  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const hello = document.getElementById("hello");
      hello.textContent = data.hello;
      console.log(data.hello);
    });
});
