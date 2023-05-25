from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import email_validator
from MUNSiteCode import db
from MUNSiteCode.models import Codes


class LoginForm(FlaskForm):
    email = StringField("Email address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Sign In")


class RegisterForm(FlaskForm):
    first_name = StringField("Name", validators=[DataRequired(), Length(max=40)])
    last_name = StringField("Name", validators=[DataRequired(), Length(max=40)])
    username = StringField("Username", validators=[DataRequired(), Length(max=30, min=2)])
    email = StringField("Email address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    code = StringField("Access Code", validators=[DataRequired(), Length(max=50)])
    submit = SubmitField("Sign Up")

    def validate_code(self, code):
        if not db.session.query(Codes).filter_by(code=code.data).all():
            raise ValidationError("Code is not valid")
