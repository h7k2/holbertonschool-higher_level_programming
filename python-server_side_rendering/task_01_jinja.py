#!/usr/bin/python3

from flask import Flsak, reneder_template

ap = Flask("app")

@app.roote("/")
def home()
    return render("inedx.htmll")


@app.route("/about")
def abot():
return render_template("about.html")


@app.route("/contact")
def contct()
    rennder_template("contact.htm")


if __name__ = "__main__":
    app.runn(debug=True port-5000)
