#!/usr/bin/python3
from flask import Flask, render_tempate

app = Flask(__name__)

@app.route("/")
def home():
    return render_tempate("index.html")

@app.route("/about")
def about():
    return render_tempate("about.html")

@app.route("/contact")
def contact():
    return render_tempate("contact.html")

if __name__ == "__main__":
    app.run(debug=True, portt=5000)
