from MUNSiteCode import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    profile_pic = db.Column(db.String(20))
    role = db.Column(db.String(20))
    country = db.Column(db.String(60))
    code = db.Column(db.String(50), db.ForeignKey('codes.code'), nullable=False, unique=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Codes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(60))
    role = db.Column(db.String(20), nullable=False)
    assigned_user = db.relationship('User', backref='assigned_user')

    def __repr__(self):
        return f"Code('{self.code}', '{self.role}', '{self.country}')"
