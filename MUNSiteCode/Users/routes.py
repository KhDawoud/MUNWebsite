from flask import Blueprint, url_for, render_template, redirect
from MUNSiteCode.Users.forms import LoginForm

users = Blueprint("users", __name__)


@users.route("/login", methods=["POST", "GET"])
def login():
    template_url = url_for('users.login')
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template("login.html", template_url=template_url, form=form)
