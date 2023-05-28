from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import email_validator
from MUNSiteCode import db
from MUNSiteCode.models import Codes, User
from flask_login import current_user


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
        if not db.session.query(Codes).filter_by(code=code.data).first():
            raise ValidationError("Code is not valid")
        if db.session.query(User).filter_by(code=code.data).first():
            raise ValidationError("Code is already in use")

    def validate_username(self, username):
        if db.session.query(User).filter_by(username=username.data).first():
            raise ValidationError("This username is taken")

    def validate_email(self, email):
        if db.session.query(User).filter_by(email=email.data).first():
            raise ValidationError("This email is already in use")


class UpdateProfilePicForm(FlaskForm):
    profile_pic = FileField('Profile Picture', validators=[DataRequired(), FileAllowed(["jpg", "png", "jpeg"],
                                                                                       "File must be a PNG or JPG")])
    submit = SubmitField('Save Changes')


