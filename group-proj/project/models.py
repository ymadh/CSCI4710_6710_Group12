from . import db


class User(db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    is_active = db.Column(db.Boolean)

    def get_id(self):
        # returns the user e-mail
        return self.id

    def is_authenticated(self):
        return self._authenticated


class Scooters(db.Model):
    scooter_id = db.Column(db.Integer, primary_key=True)
    scooter_brand = db.Column(db.String)
    available = db.Column(db.Boolean)
    location = db.Column(db.String)

    def get_id(self):
        return self.id
