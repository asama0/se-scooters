
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
    result_query = Booking.query\
        .filter(and_(Booking.date >= start_date, Booking.date <= end_date))\
        .order_by(Booking.date)\
        .all()

    # change every booking to a dictionary
    result_dict = [
        { 'date': str(booking.date),
        'amount': booking.amount,
        'duration': booking.duration }
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




#---------------------------------------------------------#

start_year = int(datetime.today().strftime('%Y'))
start_month = int((datetime.today().strftime('%m')))
start_day = int((datetime.today().strftime('%d')))






## WEEK
day_1, day_2, day_3, day_4, day_5, day_6, day_7 = 0, 0, 0, 0, 0, 0, 0
sum=0

# pass days between to store sumes in the list , ex  January to February and so on
def get_data_list_days(period_list_start, period_list_end):

    period = query_booking_by_date(
        (datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(days=period_list_start)),
        datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(days=period_list_end))
    # sum for lenth
    global sum
    sum = 0

    for i in period:
        sum = sum + i.get("amount")




get_data_list_days(10000, 9500)
day_1, day_2, day_3 = sum, sum, 50

print(day_1)
print(day_2)
print(day_3)
print(day_4)



# p = [50.33, 10.22222222, 4, 4, 19, 4, 14, 99]
week = [day_1, day_2, day_3, day_4, day_5, day_6, day_7]

# sending array to javascript
@app.route('/request3', methods=['POST'])
def post_request_data3():
    global p
    #return a list of integers
    return jsonify(week)





# for weekly graph
weekly_day_1 = query_booking_by_date((datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(days=7)),
                           datetime(start_year, start_month, start_day))



# for monthly graph
monthly = query_booking_by_date((datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(months=7)),
                           datetime(start_year, start_month, start_day))

#for yearly graph
yearly = query_booking_by_date((datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(years=7)),
                           datetime(start_year, start_month, start_day))











# print(datetime.today() - dateutil.relativedelta.relativedelta(months= 10))
#print(start_year, start_month, start_day)

#
# ssstart = str(datetime.today())
# print(ssstart.replace("-", ","))
# print(datetime.today() - timedelta(6))






