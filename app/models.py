from email.policy import default
from app import db,app
from flask_login import UserMixin
from sqlalchemy.sql.functions import now
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


   
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
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
    def get_reset_token(self, expires_sec=1000):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
        
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
