// When the user clicks on #red_header, add the class 'red' to the <header>
document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});
