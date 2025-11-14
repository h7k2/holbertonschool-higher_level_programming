📌 Project: Python – Server-Side Rendering

Curriculum: Holberton School — Foundations v2.1
Skills: Python, Flask, Jinja2, JSON, CSV, SQLite
Topics: Templating, SSR, Data Rendering, Routes, Files, Databases

🚀 Introduction

This project introduces Server-Side Rendering (SSR) using Python and the Flask micro-framework.
SSR generates fully-rendered HTML pages on the server before sending them to the client, resulting in:

Better SEO

Faster first paint

Simpler state management

More secure data handling

Throughout this project, you will learn how to:

Build SSR applications in Flask

Use the Jinja2 templating engine

Render dynamic content

Read data from JSON, CSV, and SQLite

Build reusable templates

Handle errors gracefully

🎯 Learning Objectives

By completing this project, you will be able to:

Explain server-side vs client-side rendering

Create Flask routes and render HTML pages

Use Jinja2 for dynamic templates

Build reusable HTML components with {% include %}

Render dynamic lists using loops

Handle conditional content in templates

Load and parse JSON files

Work with CSV files

Read from an SQLite database

Display filtered or full datasets through a single template

📂 Project Structure
python-server_side_rendering/
│
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
│
├── template.txt
├── items.json
├── products.json
├── products.csv
├── products.db
│
└── templates/
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── header.html
    ├── footer.html
    ├── items.html
    └── product_display.html

📘 Task Overview
✅ Task 0: Creating a Simple Templating Program

Implement the function:

generate_invitations(template, attendees)

The function must:

Validate input types

Handle empty template / empty data list

Replace placeholders:

{name}, {event_title}, {event_date}, {event_location}

Replace missing values with "N/A"

Generate output files:

output_1.txt
output_2.txt
output_3.txt


This task simulates basic SSR logic without Flask.

✅ Task 1: Basic Flask App + Jinja Template

Create a Flask app (task_01_jinja.py) with:

A route / rendering index.html

A templates/ folder containing:

index.html

header.html

footer.html

about.html

contact.html

Use:

{% include 'header.html' %}
{% include 'footer.html' %}


Routes:

/

/about

/contact

This task introduces:

Jinja rendering

Template inclusion

Multi-page Flask apps

✅ Task 2: Dynamic Template with Loops & Conditions

Create items.html with:

A Jinja loop {% for item in items %}

A condition {% if items %} … {% else %} No items found. {% endif %}

Add route /items in Flask:

Load “items.json”

Pass the data to the template

This teaches:

Conditional rendering

Loops in Jinja

Dynamic SSR content

✅ Task 3: Rendering Data From JSON or CSV

Add route:

/products?source=json
/products?source=csv
/products?source=json&id=2


The app must:

Read products.json if source=json

Read products.csv if source=csv

Filter by id if provided

Handle “Wrong source” errors

Handle “Product not found”

Use one shared template: product_display.html

Shows:

Query parameters

File reading

Data filtering

Dynamic tables

✅ Task 4: Adding SQLite Database Rendering

Extend the /products route:

Add support for:

source=sql


Read from “products.db”

Use the same product_display.html

Handle:

Wrong source

Database errors

Missing ID

Demonstrates:

Database querying

Unified SSR rendering

Multiple data sources into one template

🛠️ Running the Project
Install Flask:
pip install Flask

Run a task:

Task 1

python3 task_01_jinja.py


Task 2

python3 task_02_logic.py


Task 3

python3 task_03_files.py


Task 4

python3 task_04_db.py

Access in browser:
http://localhost:5000/

🛠️ Technologies Used

Python 3

Flask

Jinja2

JSON

CSV

SQLite3

HTML5
