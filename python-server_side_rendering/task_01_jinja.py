#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # fonctionne, juste un petit espace inutile
    return render_template("index.html")

@app.route("/about")
def about():
    # fonctionne même si le nom est simple
    return render_template("about.html")

@app.route("/contact")
def contact():
    # pareil : fonctionne mais c’est minimaliste
    return render_template("contact.html")

if __name__ == "__main__":
    # marche bien, juste debug=True (débutant garde ça allumé)
    app.run(debug=True, port=5000)
