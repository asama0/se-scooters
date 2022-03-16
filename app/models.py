from app import db
from flask_login import UserMixin
from sqlalchemy.sql.functions import now
from flask_admin import BaseView, expose

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    privilege = db.Column(db.Integer, nullable=False, default=1)
    bookings = db.relationship('Booking', backref='user')
    blocked = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<User #{self.id} {self.name}>'

class Scooter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.Boolean, nullable=False)
    bookings = db.relationship('Booking', backref='scooter')
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'))

    def __repr__(self):
        return f'<Scooter #{self.id}>'

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    pickup_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Float, nullable=False)

    created_date_time = db.Column(db.DateTime(timezone=True), default=now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooter.id'), nullable=False)

    def __repr__(self):
        return f'<Booking #{self.id}>'

class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(120), unique=True, nullable=False)
    scooters = db.relationship('Scooter', backref='parking')
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return str(self.location)

class Cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return str(self.duration)

class Analytics(BaseView):
    @expose('/')
    def index(self):
        return self.render('analytics_index.html')



