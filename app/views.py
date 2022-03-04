
from flask import render_template
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from flask import jsonify

from app import app, db, admin
from .models import *

from sqlalchemy import and_
import random
from pprint import pprint

# add models to admin page
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Scooter, db.session))
admin.add_view(ModelView(Parking, db.session))
admin.add_view(ModelView(Cost, db.session))

@app.route('/')
def index():

    return render_template('index.html')

def query_booking_by_date(start_date, end_date):
    result_query = Booking.query\
        .filter(and_(Booking.date >= start_date, Booking.date <= end_date))\
        .order_by(Booking.date)\
        .all()

    result_dict = [
    {
        'date': str(booking.date),
        'amount': booking.amount,
        'duration': booking.duration
    }
    for booking in result_query
    ]

    return result_dict


# for _ in range(20):
#     db.session.add(Booking(
#         amount=random.randrange(1,200) + random.random(),
#         date=datetime(
#             random.randrange(1980,2021),
#             random.randrange(1,12),
#             random.randrange(1,28),
#             random.randrange(0,23),
#             random.randrange(0,23),
#             random.randrange(0,59),
#             random.randrange(0,59)
#             ),
#         duration=random.randrange(1,4),
#         )
#     )

db.session.commit()

# pprint(query_booking_by_date(datetime(1980, 1, 1), datetime(2021, 12, 31)))

pprint(query_booking_by_date(datetime(2015, 1, 1), datetime(2021, 12, 31)))
