from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from MUNSiteCode.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = "users.login"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    from MUNSiteCode.Main.routes import main
    from MUNSiteCode.Posts.routes import posts
    from MUNSiteCode.Users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(users)

    return app
