$(function () {
  $('#btn_translate').click(translate);
  $('input#language_code').keypress((e) => {
    if (e.key === 'Enter') translate();
  });
});

function translate () {
  const $lang = $('input#language_code').val();
  const $url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $.ajax({
    url: $url + $lang,
    type: 'GET',
    success: (data) => {
      $('#hello').text(data.hello);
    }
  });
}
