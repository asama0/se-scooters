from app import db
<<<<<<< HEAD

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
=======
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
>>>>>>> 4811a66096e30df993263933fda8ddd7b7e30684
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
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooter.id'))

    def __repr__(self):
        return f'<Booking #{self.id}>'

class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(120), unique=True, nullable=False)
    scooters = db.relationship('Scooter', backref='parking')
<<<<<<< HEAD
=======
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
>>>>>>> 4811a66096e30df993263933fda8ddd7b7e30684

    def __repr__(self):
        return f'<Parking #{self.id} {self.location}>'

class Cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
<<<<<<< HEAD
        return f'<Cost #{self.id} t={self.duration} ${self.duration}>'
=======
        return f'<Cost #{self.id} t={self.duration} ${self.duration}>'
>>>>>>> 4811a66096e30df993263933fda8ddd7b7e30684
