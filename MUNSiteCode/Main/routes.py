from flask import render_template, redirect, url_for, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")
