from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import current_user, login_required
from app import app, db
from datetime import timedelta

from .models import *
from .forms import *
from stripe_functions import *
from helper_functions import *


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/activate/<token>', methods=['GET', 'POST'])
def activate(token):
    if request.method == 'POST':
        qr_result = request.form['qr_result']
        if token == qr_result:
            flash('Enjoy the ride!', category='alert-success')
        else:
            flash('QR code scanning failed.', category='alert-danger')

        return redirect(url_for('booking_views.dashboard'))

    return render_template('QRCodeScanner.html')


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = editProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.phone = form.phone.data
        current_user.birth_date = form.birth_date.data
        db.session.commit()
        flash("Updated Successfully!", category='alert-success')
    else:
        flash_errors(form)
    return render_template('account.html', page_name='account', form=form)


@app.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    form = feedbackForm()

    # retrieve the feedback then adds it to the database
    if form.validate_on_submit():
        feedback = Feedback(
            experience=form.experience.data,
            feedback=form.feedback.data,
            user_id=current_user.id
        )
        print(feedback)
        db.session.add(feedback)
        db.session.commit()
        flash('Feedback submitted successfully', category='alert-success')
    else:
        flash_errors(form)

    return render_template('feedback.html', page_name='feedback', form=form)


one_week = timedelta(days=7)
one_day = timedelta(days=1)
one_hour = timedelta(seconds=3600)

@app.route('/not_available_times', methods=['POST'])
@login_required
def not_available_times():
    global one_day
    form = NotAvailableTimesForm()

    if form.validate_on_submit():
        parking_id = form.pickup_parking_id.data
        date = form.pickup_date.data

        bookings = Booking.query.filter(
            ( Booking.parking_id == parking_id ) &
            ( date - one_week <= Booking.pickup_date ) &
            ( Booking.pickup_date <= date + one_day )
        )

        times_to_disable = {'all':False}

        for booking in bookings:
            booking_duration = booking.get_timedelta()

            if  booking_duration >= one_day:
                return jsonify({'all':True})
            elif booking.pickup_date == date:
                times_to_disable[booking.pickup_date.strftime("%H:00")] = booking_duration

        return jsonify(times_to_disable)

    return "The server refuses the attempt to brew coffee with a teapot.", 418

@app.route('/not_available_durations', methods=['POST'])
@login_required
def not_available_durations():
    form = NotAvailableDurationsForm()

    if form.validate_on_submit():
        booking = Booking.query.get(form.booking_id.data)

        durations_to_disable = []

        for price in Price.query.all():
            if Booking.query.filter(
            ( Booking.id != booking.id ) &
            ( Booking.scooter_id == booking.scooter_id ) &
            ( Booking.pickup_date <= ( booking.pickup_date + price.get_timedelta() ) )
            ).all():
                durations_to_disable.append(price.id)

        return jsonify(durations_to_disable)

    return "The server refuses the attempt to brew coffee with a teapot.", 418