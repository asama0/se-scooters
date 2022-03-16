import numpy as np
from app.models import Booking
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
        {'date': str(booking.created_date_time),
         'amount': booking.amount,
         'duration': booking.duration}
        for booking in result_query
    ]

    return result_dict

def get_full_data():
    resssult = Booking.query.filter((Booking.id >= 1) & (Booking.created_date_time <= datetime(start_year, start_month, start_day)))

    # change every booking to a dictionary
    result_dict = [
        {'date': str(booking.created_date_time),
         'amount': booking.amount,
         'duration': booking.duration}
        for booking in resssult
    ]

    return result_dict

# pass days between to store sumes in the list , ex  January to February and so on
def get_data_list_days(period_list_start, period_list_end, period_key):
    if period_key == "week":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) - relativedelta(days=period_list_start)),
            datetime(start_year, start_month, start_day) - relativedelta(days=period_list_end))
    elif period_key == "month":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) - relativedelta(days=period_list_start)),
            datetime(start_year, start_month, start_day) - relativedelta(days=period_list_end))
    elif period_key == "year":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) - relativedelta(months=period_list_start)),
            datetime(start_year, start_month, start_day) - relativedelta(months=period_list_end))
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

week.insert(1, 111)
month.insert(2, 30)
