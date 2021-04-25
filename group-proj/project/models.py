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
        return self.scooter_id


class Renters(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    currently_using = db.Column(db.Boolean)

    def get_id(self):
        return self.user_id


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    scooter_id = db.Column(db.String)
    rental_num = db.Column(db.Integer)
    rent_date = db.Column(db.DateTime, server_default=db.func.now())
    return_date = db.Column(db.DateTime, nullable=True)

    def get_id(self):
        return self.id
