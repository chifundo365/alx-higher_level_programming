$(function(){
  const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json"
  $.ajax({
    type: 'GET',
    url: url,
    success: (data) => {
        $('#character').text(data.name);
    }
  });
});