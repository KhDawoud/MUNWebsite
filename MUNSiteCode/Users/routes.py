from flask import Blueprint, url_for, render_template
from MUNSiteCode.Users.forms import LoginForm

users = Blueprint("users", __name__)


@users.route("/login")
def login():
    template_url = url_for('users.login')
    form = LoginForm()
    return render_template("login.html", template_url=template_url, form=form)
