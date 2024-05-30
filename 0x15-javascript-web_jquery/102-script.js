$(function () {
  const $url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('#btn_translate').click(() => {
    const $lang = $('input#language_code').val();
    $.ajax({
      url: $url + $lang,
      type: 'GET',
      success: (data) => {
        $('#hello').text(data.hello);
      }
    });
  });
});
