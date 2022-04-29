from app import db, app
from flask_login import UserMixin
from sqlalchemy.sql.functions import now
import jwt
from datetime import datetime, timedelta
from time import time
from helper_functions import string_to_timedelta


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    stripe_id = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    privilege = db.Column(db.Integer, nullable=False, default=1)
    blocked = db.Column(db.Boolean, nullable=False, default=False)

    bookings = db.relationship('Booking', backref='user')
    feedbacks = db.relationship('Feedback', backref='user')

    def __repr__(self):
        return f'<User #{self.id}>'

    # for password reset
    def get_reset_token(self, expires=1000):
        return jwt.encode(
            {'reset_password': self.email, 'exp': time() + expires},
            key=app.config['SECRET_KEY']
        )

    @staticmethod
    def verify_reset_token(token):
        try:
            email = jwt.decode(token, key=app.config['SECRET_KEY'],  algorithms=[
                               "HS256"])['reset_password']
        except Exception as e:
            print(e)
            return
        return User.query.filter_by(email=email).first()


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
    scooter_id = db.Column(db.Integer, db.ForeignKey(
        'scooter.id'), nullable=False)
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)
    price_id = db.Column(db.Integer, db.ForeignKey('price.id'), nullable=False)
    payment_intent = db.Column(db.String(100), unique=True)

    def get_end_datetime(self):
        return self.pickup_date + Price.query.get(self.price_id).get_timedelta()

    def get_timedelta(self):
        return Price.query.get(self.price_id).get_timedelta()

    def __repr__(self):
        return f'<Booking #{self.id}>'


class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    scooters = db.relationship('Scooter', backref='parking')
    bookings = db.relationship('Booking', backref='parking')

    def is_full(self, date_time:datetime):
        num_scooters = len(self.scooters)
        scooters_booked = set()

        for booking in self.bookings:
            if booking.pickup_date == date_time:
                scooters_booked.add(booking.scooter_id)
            elif booking.pickup_date <= date_time and date_time < booking.get_end_datetime():
                scooters_booked.add(booking.scooter_id)

        return len(scooters_booked) >= num_scooters

    def get_full_days(self, opening_hour:timedelta, closing_hour:timedelta,
        start_date:datetime=datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
        end_date:datetime=datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        +timedelta(days=21)):
        one_day = timedelta(days=1)
        one_hour = timedelta(hours=1)
        day = start_date
        day_hour = opening_hour

        result:'dict[str, list]' = dict()

        while day <= end_date:
            day_hour = opening_hour
            day_iso_str = day.date().isoformat()

            while day_hour <= closing_hour:
                if self.is_full( day+day_hour ):
                    if day_iso_str not in result:
                        result[day_iso_str] = []

                    result[day_iso_str].append(day_hour.seconds//3600 )
                day_hour += one_hour

            day += one_day

        return result

    def __repr__(self):
        return str(self.name)


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_id = db.Column(db.String(100), unique=True)
    lookup_key = db.Column(db.String(100), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    bookings = db.relationship('Booking', backref='price')

    def get_timedelta(self):
        return string_to_timedelta(self.lookup_key)

    def __repr__(self):
        return str(self.lookup_key)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    experience = db.Column(db.String(10), nullable=False)
    feedback = db.Column(db.String(10000), nullable=False)
    urgent = db.Column(db.Boolean, default=False, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Feedback #{self.id}>'
