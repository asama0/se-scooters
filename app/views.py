from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import current_user, login_required
from datetime import datetime
import stripe
from app import app, db

from .models import *
from .forms import *
from stripe_functions import *
from helper_functions import *
from analytics_quries import *

new_booking:Booking

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    global new_booking
    checkout_status = request.args['checkout_status'] if 'checkout_status' in request.args else ''

    if request.method == 'GET':
        if checkout_status == 'canceled':
            flash('Payment session was canceled.')
        elif checkout_status == 'success':
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking was saved successfuly.', category='alert-success')
            new_booking = None

    form = BookingForm()

    if form.validate_on_submit():

        pickup_date = datetime.combine(form.pickup_date.data, form.pickup_time.data)
        scooter_chosen = Scooter.query.filter(
                            (Scooter.availability==True)&\
                            (Scooter.parking_id==form.pickup_parking_id.data)
                        ).first()
        price_used = form.time_period.data

        new_booking = Booking(
            pickup_date= pickup_date,
            user_id = current_user.id,
            scooter_id = scooter_chosen.id,
            price_id = price_used.id
        )

        return redirect(url_for('checkout', _method='POST', price_api_id=form.time_period.data.api_id), code=307)

    else:
        flash_errors(form)

    parkings = Parking.query.filter(Parking.scooters.any()).all()

    return render_template('dashboard.html', form=form, parkings=parkings, page_name='dashboard')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html', page_name='tickets')

@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('account.html', page_name='account')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    return render_template('feedback.html', page_name='feedback')




@app.route('/checkout', methods=['POST'])
def checkout():
    price_api_id = request.args['price_api_id']
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

