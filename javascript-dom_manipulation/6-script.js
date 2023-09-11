fetch("https://swapi-api.hbtn.io/api/people/5/?format=json") // Replace with the URL you want to fetch data from
  .then((response) => {
    // Check if the response status is OK (HTTP status code 200)
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    // Parse the response as JSON
    return response.json();
  })
  .then((data) => {
    // Use the retrieved data
    const characterElement = document.getElementById("character");
    characterElement.textContent = data.name;
  })
  .catch((error) => {
    // Handle any errors that occurred during the fetch
    console.error("Fetch error:", error);
  });
