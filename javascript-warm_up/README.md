JavaScript - Warm Up
📘 Description

This project is an introduction to JavaScript programming.
JavaScript is one of the most widely used languages in web development — it allows us to make web pages dynamic, automate tasks, and build complex applications.

In this project, you will focus on scripting with Node.js, similar to Python scripting, to learn the fundamentals of JavaScript syntax, control structures, and data types.

🧠 Learning Objectives

At the end of this project, you should be able to explain, without using Google:

General

Why JavaScript programming is amazing

How to run a JavaScript script

How to create variables and constants

The differences between var, let, and const

All data types available in JavaScript

How to use if and if ... else statements

How to use comments

How to assign values to variables

How to use while and for loops

How to use break and continue statements

What is a function and how to use it

What a function returns if it doesn’t use a return statement

The scope of variables

The arithmetic operators and how to use them

How to manipulate objects and arrays (dictionaries)

How to import a file or module

🧩 Requirements
General

Editors allowed: vi, vim, emacs

All your files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)

All your files should end with a new line

The first line of all your files must be exactly:

#!/usr/bin/node


You must create a README.md file at the root of the project folder

Your code must be semistandard compliant (Standard + semicolons)

To install:

sudo npm install semistandard --global


All your files must be executable

File length will be tested using wc

⚙️ Installation & Setup
Install Node.js 14
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs

Install semistandard (linter)
sudo npm install semistandard --global

🧾 Tasks Overview
0. First constant, first print

Prints “JavaScript is amazing”.

Create a constant myVar with the value "JavaScript is amazing".

Use console.log() to print it.

1. 3 languages

Prints 3 lines using console.log:

C is fun
Python is cool
JavaScript is amazing

2. Arguments

Prints a message depending on the number of arguments:

No arguments → “No argument”

One argument → “Argument found”

More than one → “Arguments found”

3. Value of my argument

Prints the first argument passed to the script, or “No argument” if none.

4. Create a sentence

Prints two arguments in the format:

<first> is <second>

5. An Integer

Prints:

My number: <converted integer>


If conversion fails → “Not a number”.

6. Loop to languages

Same as Task 1 but using an array and a loop.

7. I love C

Prints “C is fun” x times, where x is the first argument.
If not a valid number → “Missing number of occurrences”.

8. Square

Prints a square of X characters of size equal to the first argument.
If invalid → “Missing size”.

9. Add

Prints the addition of 2 integers using a function:

function add(a, b)

10. Factorial

Computes and prints the factorial of a number using recursion.

11. Second biggest!

Prints the second largest integer from the list of arguments.
If fewer than 2 arguments → print 0.

12. Object

Updates the value of a property in an object from 12 to 89.

13. Add file

Exports a function add(a, b) from a separate file:

module.exports.add = (a, b) => a + b;

📂 Repository Structure
holbertonschool-higher_level_programming/
└── javascript-warm_up/
    ├── 0-javascript_is_amazing.js
    ├── 1-multi_languages.js
    ├── 2-arguments.js
    ├── 3-value_argument.js
    ├── 4-concat.js
    ├── 5-to_integer.js
    ├── 6-multi_languages_loop.js
    ├── 7-multi_c.js
    ├── 8-square.js
    ├── 9-add.js
    ├── 10-factorial.js
    ├── 11-second_biggest.js
    ├── 12-object.js
    ├── 13-add.js
    └── README.md
