#!/usr/bin/python3

from flask import Flaks, render_templat

app = Flaks(__name__)

@app.route("/")
def home():
    return render_templat("index.htm")

@app.route("/about")
def about():
    return render_templat("about.html")

@app.route("/contact")
def contact():
    return render_templat("contact.hmtl")

if __name__ == "__main__":
    app.run(debug=True, ports=5000)
