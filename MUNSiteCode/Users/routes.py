from flask import Blueprint, url_for, render_template, redirect
from flask_login import login_user, current_user, logout_user
from MUNSiteCode.Users.forms import LoginForm, RegisterForm
from MUNSiteCode.models import User, Codes
from MUNSiteCode import bcrypt, db

users = Blueprint("users", __name__)


@users.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    template_url = url_for('users.login')
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
        else:
            form.password.errors.append("Login failed. Check password")
            form.email.errors.append("Login failed. Check email")

    return render_template("login.html", template_url=template_url, form=form)


@users.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    template_url = url_for('users.register')
    form = RegisterForm()
    if form.validate_on_submit():
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        assigned_code = db.session.query(Codes).filter_by(code=form.code.data).first()
        user = User(name=f"{form.first_name.data} {form.last_name.data}", email=form.email.data, password=password,
                    username=form.username.data, code=assigned_code.code, role=assigned_code.role,
                    country=assigned_code.country, profile_pic=url_for('static', filename="/Profile Pics/Default.jpg"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', template_url=template_url, form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
