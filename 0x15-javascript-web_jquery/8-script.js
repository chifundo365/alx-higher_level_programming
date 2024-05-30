$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.ajax({
    type: 'GET',
    url,
    success: (data) => {
      $.each(data.results, (i, movie) => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        $('#list_movies').append(li);
      });
    }
  });
});
