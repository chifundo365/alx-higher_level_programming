$(function(){
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'
  $.ajax({
    type: 'GET',
    url: url,
    success: (data) => {
        $.each(data.results, (i, movie) => {
            let li = document.createElement('li');
            li.textContent = movie.title;
            $('#list_movies').append(li);
        });
    }
  });
});