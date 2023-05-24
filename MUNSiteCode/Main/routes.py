from flask import render_template, redirect, url_for, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    template_url = url_for("main.home")
    return render_template("home.html", template_url=template_url)


@main.route("/blog")
def blog():
    template_url = url_for("main.blog")
    return render_template("blog.html", template_url=template_url)
