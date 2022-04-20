import numpy as np
from app.models import Booking, Price
from datetime import datetime
from dateutil.relativedelta import relativedelta

start_year = int(datetime.today().strftime('%Y'))
start_month = int((datetime.today().strftime('%m')))
start_day = int((datetime.today().strftime('%d')))

week = []
month = []
year = []
max_period = []
sum = 0


def query_booking_by_date(start_date, end_date):
    # querying bookings from database
    result_query = Booking.query \
        .filter((Booking.created_date_time >= start_date) & (Booking.created_date_time <= end_date)) \
        .order_by(Booking.created_date_time) \
        .all()

    # change every booking to a dictionary
    result_dict = [
        {
            'date': str(booking.created_date_time),
            'amount': Price.query.get(booking.price_id).amount,
            'duration': Price.query.get(booking.price_id).get_timedelta().seconds//3600
        } for booking in result_query
    ]

    return result_dict


one_h = 0
four_h = 0
one_week = 0
one_day = 0


def popular_time_find():
    global one_day
    global four_h
    global one_week
    global one_h
    one_h = 0
    four_h = 0
    one_week = 0
    one_day = 0
    somedata = get_full_data()
    print(somedata)
    pop = 0
    for i in somedata:
        pop = 0
        pop = i.get("duration")
        if pop == 168:
            one_week += 1
        elif pop == 24:
            one_day += 1
        elif pop == 4:
            four_h += 1
        elif pop == 1:
            one_h += 1






def get_full_data():
    resssult = Booking.query.all()

    # change every booking to a dictionary
    result_dict = [
        {'date': str(booking.created_date_time),
         'amount': Price.query.get(booking.price_id).amount,
         'duration': Price.query.get(booking.price_id).get_timedelta().seconds//3600+
                     24*Price.query.get(booking.price_id).get_timedelta().days//1}
        for booking in resssult
    ]

    return result_dict

# pass days between to store sumes in the list , ex  January to February and so on


def get_data_list_days(period_list_start, period_list_end, period_key):
    global max_period
    if period_key == "total":
        max_period = []



    if period_key == "week":
        period = query_booking_by_date(
            datetime(start_year, start_month, start_day) -
            relativedelta(days=period_list_start),
            datetime(start_year, start_month, start_day) -
            relativedelta(days=period_list_end)
        )

    elif period_key == "month":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) -
             relativedelta(days=period_list_start)),
            datetime(start_year, start_month, start_day) - relativedelta(days=period_list_end))

    elif period_key == "year":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) -
             relativedelta(months=period_list_start)),
            datetime(start_year, start_month, start_day) - relativedelta(months=period_list_end))

    elif period_key == "total":
        period = np.array_split(get_full_data(), 10)

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

    # print('max_period',max_period)


def get_analitics(period, period_key):
    global week
    global month
    global year
    if period_key == "week":
        week = []
    elif period_key == "month":
        month = []
    elif period_key == "year":
        year = []

    sum_of_period = 0

    for i in range(period):
        sum_of_period = 0

        if period_key == "week":
            sum_of_period = get_data_list_days(i, i-1, period_key)
            week.append(sum_of_period)
        elif period_key == "month":
            sum_of_period = get_data_list_days(i, i-1, period_key)
            month.append(sum_of_period)
        elif period_key == "year":
            sum_of_period = get_data_list_days(i, i-1, period_key)
            year.append(sum_of_period)

    # print('week',week)
    # print('month',month)
    # print('year',year)


# week.insert(1, 111)
# week.insert(2, 111)
# week.insert(4, 111)
# month.insert(5, 30)
# year.insert(4, 1190)
# max_period.insert(3, 212)
# year.insert(4, 700)

# popular_time_find()
# print(one_h)
# print(one_day)
# print(one_week)
# print(four_h)