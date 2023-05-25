from flask import Blueprint, url_for, render_template, redirect
from MUNSiteCode.Users.forms import LoginForm, RegisterForm

users = Blueprint("users", __name__)


@users.route("/login", methods=["POST", "GET"])
def login():
    template_url = url_for('users.login')
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template("login.html", template_url=template_url, form=form)


@users.route("/register", methods=["POST", "GET"])
def register():
    template_url = url_for('users.register')
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('users.login'))
    return render_template('register.html', template_url=template_url, form=form)
