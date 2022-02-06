from email.policy import default
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    payments = db.relationship('Payment', backref='user')
    blocked = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<User #{self.id} {self.name}>'

class Scooter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.Boolean, nullable=False)
    bookings = db.relationship('Payment', backref='scooter')
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'))

    def __repr__(self):
        return f'<Scooter #{self.id}>'

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooter.id'))

    def __repr__(self):
        return f'<Payment #{self.id}>'

class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(120), unique=True, nullable=False)
    scooters = db.relationship('Scooter', backref='parking')

    def __repr__(self):
        return f'<Parking #{self.id} {self.location}>'