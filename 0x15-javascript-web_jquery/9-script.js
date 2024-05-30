$(function () {
  const $url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.ajax({
    type: 'GET',
    url: $url,
    success: (data) => {
      $('#hello').text(data.hello);
    }
  });
});
