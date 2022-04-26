from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import current_user, login_required
from app import app, db

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
        feedback = Feedback(experience=form.experience.data,
                            feedback=form.feedback.data,
                            user_id=current_user.id)
        db.session.add(feedback)
        db.session.commit()
        flash('Feedback submitted successfully', category='alert-success')
    else:
        flash_errors(form)

    return render_template('feedback.html', page_name='feedback', form=form)

@app.route('/not_available_times', methods=['POST'])
@login_required
def not_available_times():
    form = NotAvailableTimesForm()

    if form.validate_on_submit():
        parking_id = form.pickup_parking_id.data
        date = form.pickup_date.data

        parking = Parking.query.get(parking_id)

        bookings = []
        for scooter in parking.scooters:
            bookings = Booking.query.filter_by(scooter_id=scooter.id, pickup_date=date)

        return jsonify({
            booking.pickup_date: booking.price_id
            for booking in bookings
        })

    return "The server refuses the attempt to brew coffee with a teapot.", 418