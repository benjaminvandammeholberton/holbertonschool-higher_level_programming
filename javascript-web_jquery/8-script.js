$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      console.log(data);
      data.results.forEach(function (item) {
        $('UL#list_movies').append(`<li>${item.title}</li>`);
      });
    }
  });
});
