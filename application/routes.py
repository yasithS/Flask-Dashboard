from application import app
from flask import render_template

@app.route("/")
def indeex():
    return render_template("index.html", title="Home Page")

@app.route("/base")
def layout():
    return render_template("base.html")