// Select the element with id "update_header"
const updateHeader = document.querySelector('#update_header');

// Add a click event listener to this element
updateHeader.addEventListener('click', () => {
  // When clicked, change the text of the <header> element
  document.querySelector('header').textContent = 'New Header!!!';
});
