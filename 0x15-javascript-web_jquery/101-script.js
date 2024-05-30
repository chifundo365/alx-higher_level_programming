$(function () {
  $('#add_item').click(addItem);
  $('#remove_item').click(removeItem);
  $('#clear_list').click(clearList);
});

function addItem () {
  $('ul.my_list').append('<li>Item</li');
}

function removeItem () {
  $('ul.my_list').children().last().remove();
}

function clearList () {
  $('ul.my_list').empty();
}
