import numpy as np
from dateutil.relativedelta import relativedelta
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import login_user, current_user, login_required, logout_user # needed by auth_views
from datetime import datetime
import stripe
from app import app, db

from .models import *
from .forms import *
from stripe_functions import *
from helper_functions import *

booking_form:BookingForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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

start_year = int(datetime.today().strftime('%Y'))
start_month = int((datetime.today().strftime('%m')))
start_day = int((datetime.today().strftime('%d')))


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


week = []
month = []
year = []
max_period = []
sum = 0


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

# gets data from database and sorts it to different lists
# which are used in the graphs


# sending array to javascript
@app.route('/week_request', methods=['POST'])
def post_week_request():
    # return a list of integers
    # one week graph
    get_analitics(7, "week")
    return jsonify(week)


@app.route('/month_request', methods=['POST'])
def post_month_request():
    # return a list of integers
    # one month graph
    get_analitics(30, "month")
    return jsonify(month)


@app.route('/year_request', methods=['POST'])
def post_year_request():
    # return a list of integers
    # one year graph
    get_analitics(12, "year")
    return jsonify(year)


@app.route('/total_request', methods=['POST'])
def post_total_request():
    # return a list of integers
    # general dynamic graph
    get_data_list_days(1, 1, "total")
    return jsonify(max_period)

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    global booking_form
    checkout_status = request.args.get('checkout_status')

    if checkout_status == 'canceled':
        flash('Payment session was canceled.')
    elif checkout_status == 'success':
        if not booking_form:
            flash('Booking form was not submitted.')

        pickup_date = datetime.combine(booking_form.pickup_date.data, booking_form.pickup_time.data)
        scooter_chosen = Scooter.query.filter((Scooter.availability==True)&\
        (Scooter.parking_id==booking_form.pickup_parking_id.data)).first()
        price_used = booking_form.time_period.data

        new_booking = Booking(
            pickup_date= pickup_date,
            user_id = current_user.id,
            scooter_id = scooter_chosen.id,
            price_id = price_used.id
        )

        db.session.add(new_booking)
        db.session.commit()
        booking_form = None # form data won't be used any more
        flash('Booking was saved successfuly.')


    form = BookingForm()
    if form.validate_on_submit():
        booking_form = form
        return redirect(url_for('checkout', _method='POST'), code=307)
    else:
        flash_errors(form)

    parkings = Parking.query.filter(Parking.scooters.any()).all()

    return render_template('dashboard.html', form=form, parkings=parkings)


@app.route('/checkout', methods=['POST'])
def checkout():
    global booking_form
    price_api_id = booking_form.time_period.data.api_id
    discount_id = None  #TODO

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide price ID you would like to charge
                'price': price_api_id,
                'quantity': 1,
            },
        ],
        mode='payment',
        discounts=[{'coupon': discount_id}] if discount_id else [],
        success_url= url_for('dashboard', _external=True, checkout_status='success'),
        cancel_url= url_for('dashboard', _external=True, checkout_status='canceled'),
        customer = current_user.stripe_id,
    )

    return redirect(checkout_session.url)

