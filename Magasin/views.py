from flask import redirect, render_template, url_for
from .app import app

@app.route("/")
def home():

    return render_template("home.html")
