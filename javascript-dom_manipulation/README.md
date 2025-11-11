🧠 JavaScript – DOM Manipulation
📚 Description

This project introduces DOM manipulation in pure JavaScript.
You will learn how to select, modify, and update HTML elements dynamically, listen to user events, and make HTTP requests using the Fetch API — all without reloading the page.

🎯 Learning Objectives

By the end of this project, you should be able to explain to anyone, without Google:

How to select HTML elements in JavaScript

The differences between ID, class, and tag name selectors

How to modify the style of an HTML element

How to get and update the content of an element

How to add, remove, or modify elements in the DOM

How to make HTTP requests with XMLHttpRequest and Fetch API

How to listen and bind to DOM and user events

⚙️ Requirements

All files will be interpreted in Chrome (version 57.0 or later)

All files must end with a new line

A README.md file at the root of the project folder is mandatory

Your code must be semistandard compliant

Do not use var — only let or const

The page must not reload for DOM updates or data fetching

🧩 Tasks Overview
0. Color Me

📄 File: 0-script.js
Write a script that updates the text color of the <header> element to red (#FF0000).

Use document.querySelector.

1. Click and turn red

📄 File: 1-script.js
When the user clicks on the element with id="red_header", update the <header> text color to red.

2. Add .red class

📄 File: 2-script.js
When the user clicks on the element with id="red_header", add the class .red to the <header> element.

3. Toggle classes

📄 File: 3-script.js
Toggle the class of the <header> between red and green when the user clicks on the element with id="toggle_header".

The header must always have exactly one class: red or green.

4. List of elements

📄 File: 4-script.js
Add a new <li>Item</li> element to the <ul class="my_list"> when the user clicks on the element with id="add_item".

5. Change the text

📄 File: 5-script.js
Update the text of the <header> element to “New Header!!!” when the user clicks on the element with id="update_header".

6. Star Wars character

📄 File: 6-script.js
Fetch the name of a Star Wars character from the API:
https://swapi-api.hbtn.io/api/people/5/?format=json

Display the character’s name in the element with id="character".
Use the Fetch API.

7. Star Wars movies

📄 File: 7-script.js
Fetch and list the titles of all Star Wars movies from:
https://swapi-api.hbtn.io/api/films/?format=json

Display each title inside the <ul id="list_movies">.

8. Say Hello!

📄 File: 8-script.js
Fetch from https://hellosalut.stefanbohacek.com/?lang=fr and display the value of “hello” inside the element with id="hello".

The script must work even when imported inside the <head> tag.

🧠 Key Concepts Learned
Concept	Description
DOM (Document Object Model)	The browser’s tree representation of an HTML page, which can be accessed and modified with JavaScript
querySelector()	Selects the first matching element based on a CSS selector
Event listeners	Functions triggered when the user interacts with the page (clicks, typing, etc.)
Class manipulation	Add, remove, or toggle CSS classes dynamically
Fetch API	Modern way to make HTTP requests and handle responses with Promises
InnerHTML / textContent	Used to change or read an element’s text or HTML content
No page reload	DOM updates happen dynamically in the browser without reloading
🧰 Technologies Used

JavaScript (ES6)

HTML5

CSS3

Chrome Developer Tools

Fetch API

📄 Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
