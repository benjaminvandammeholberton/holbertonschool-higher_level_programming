fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
    const list_movies = document.getElementById("list_movies");
    for (const result of data.results) {
      const movie = document.createElement("li");
      movie.textContent = result.title;
      list_movies.appendChild(movie);
    }
  })
  .catch((error) => {
    console.error("Fetch error:", error);
  });
