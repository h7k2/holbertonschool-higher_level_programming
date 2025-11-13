// Fetch the Star Wars character and display the name

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    // Insert the character name in the div#character
    document.getElementById('character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
