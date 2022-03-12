import numpy as np
from flask import render_template, jsonify
from flask_admin.contrib.sqla import ModelView
from datetime import datetime, timedelta
import dateutil.relativedelta

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
    # querying bookings from database
    result_query = Booking.query \
        .filter(and_(Booking.date >= start_date, Booking.date <= end_date)) \
        .order_by(Booking.date) \
        .all()

    # change every booking to a dictionary
    result_dict = [
        {'date': str(booking.date),
         'amount': booking.amount,
         'duration': booking.duration}
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
#
# db.session.commit()

# pprint(query_booking_by_date(datetime(1980, 1, 1), datetime(2021, 12, 31)))

# pprint(query_booking_by_date(datetime(2015, 1, 1), datetime(2015, 12, 31)))


# qu = query_booking_by_date(datetime(2000, 1, 1), datetime(2015, 12, 31))
# print(qu[0]["amount"])
# print(qu)


# ---------------------------------------------------------#

start_year = int(datetime.today().strftime('%Y'))
start_month = int((datetime.today().strftime('%m')))
start_day = int((datetime.today().strftime('%d')))


def get_full_data():
    resssult = Booking.query.filter(and_(Booking.id >= 1, Booking.date <= datetime(start_year, start_month, start_day)))

    # change every booking to a dictionary
    result_dict = [
        {'date': str(booking.date),
         'amount': booking.amount,
         'duration': booking.duration}
        for booking in resssult
    ]

    return result_dict


week = []
month = []
year = []
max_period = []
sum = 0


# pass days between to store sumes in the list , ex  January to February and so on
def get_data_list_days(period_list_start, period_list_end, period_key):
    if period_key == "week":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(
                days=period_list_start)),
            datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(days=period_list_end))
    elif period_key == "month":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(
                days=period_list_start)),
            datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(days=period_list_end))
    elif period_key == "year":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(
                months=period_list_start)),
            datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(months=period_list_end))
    elif period_key == "total":
        period = np.array_split(get_full_data(), 20)

    # sum for lenth
    global sum
    sum = 0

    if period_key == "total":
        for i in period:
            sum = 0
            for j in i:
                sum = sum + j.get("amount")
            max_period.append(sum)
    else:
        for i in period:
            sum = sum + i.get("amount")
        return sum


def get_analitics(period, period_key):
    sum_of_period = 0

    for i in range(period):
        sum_of_period = 0

        if period_key == "week":
            sum_of_period = get_data_list_days(i + 1, i, period_key)
            week.append(sum_of_period)
        elif period_key == "month":
            sum_of_period = get_data_list_days(i + 1, i, period_key)
            month.append(sum_of_period)
        elif period_key == "year":
            sum_of_period = get_data_list_days(i + 1, i, period_key)
            year.append(sum_of_period)


# one week
get_analitics(7, "week")
# one month
get_analitics(30, "month")
# one year
get_analitics(12, "year")
# general dynamic graph
get_data_list_days(1, 1, "total")


# sending array to javascript
@app.route('/request3', methods=['POST'])
def post_request_data3():
    global p
    # return a list of integers
    return jsonify(week)


