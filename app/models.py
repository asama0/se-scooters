from app import db, app
from flask_login import UserMixin
from sqlalchemy.sql.functions import now
from flask_admin import BaseView, expose
import jwt
from time import time


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    stripe_id = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    privilege = db.Column(db.Integer, nullable=False, default=1)
    blocked = db.Column(db.Boolean, nullable=False, default=False)

    bookings = db.relationship('Booking', backref='user')

    def __repr__(self):
        return f'<User #{self.id} {self.name}>'

    #for password reset
    def get_reset_token(self, expires=1000):
        return jwt.encode({'reset_password': self.username, 'exp': time() + expires},
                           key=app.config['SECRET_KEY'])

    @staticmethod
    def verify_reset_token(token):
        try:
            username = jwt.decode(token, key=app.config['SECRET_KEY'])['reset_password']
            print('Verifed toker for:',username)
        except Exception as e:
            print(e)
            return
        return User.query.filter_by(username=username).first()

class Scooter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.Boolean, default=True, nullable=False)

    bookings = db.relationship('Booking', backref='scooter')
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'))

    def __repr__(self):
        return f'<Scooter #{self.id}>'

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pickup_date = db.Column(db.DateTime(timezone=True), nullable=False)
    created_date_time = db.Column(db.DateTime(timezone=True), default=now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooter.id'), nullable=False)
    price_id = db.Column(db.Integer, db.ForeignKey('price.id'), nullable=False)

    def __repr__(self):
        return f'<Booking #{self.id}>'

class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(120), unique=True, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)

    scooters = db.relationship('Scooter', backref='parking')

    def __repr__(self):
        return str(self.location)

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_id = db.Column(db.String(100), unique=True, nullable=False)
    lookup_key = db.Column(db.String(100), unique=True, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    bookings = db.relationship('Booking', backref='price')

    def __repr__(self):
        return str(self.lookup_key)

class Analytics(BaseView):
    @expose('/')
    def index(self):
        return self.render('analytics_index.html')
