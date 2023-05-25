from MUNSiteCode import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(20))
    country = db.Column(db.String(60))
    code = db.relationship(db.String(50), db.ForeignKey('codes.code'), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Codes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(60))
    role = db.String(db.String(20), nullable=False)
    user = db.relationship('User', backref='code')

    def __repr__(self):
        return f"Code('{self.code}', '{self.role}', '{self.country}')"
