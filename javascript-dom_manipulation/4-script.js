// When the user clicks on #add_item, add a new <li>Item</li> to the list .my_list
document.querySelector('#add_item').addEventListener('click', function () {
  const list = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
