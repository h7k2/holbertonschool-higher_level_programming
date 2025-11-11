// When the user clicks on #toggle_header, toggle the class of <header> between red and green
document.querySelector('#toggle_header').addEventListener('click', function () {
  const header = document.querySelector('header');

  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
