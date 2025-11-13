// Run the code only after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      // Display the translated "hello" in the element with id="hello"
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching hello:', error);
    });
});
