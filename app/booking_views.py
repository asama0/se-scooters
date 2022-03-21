from flask import Blueprint, render_template, url_for, flash, redirect, request
from datetime import date, datetime
import stripe

from app import db
from .views import current_user, login_required
from .models import *
from .forms import *
from stripe_functions import *
from helper_functions import *


booking_views = Blueprint('booking_views', __name__, static_folder='static', template_folder='template')

new_booking = None

@booking_views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    global new_booking
    checkout_status = request.args['checkout_status'] if 'checkout_status' in request.args else ''

    if request.method == 'GET' and new_booking:
        if checkout_status == 'canceled':
            flash('Payment session was canceled.')
        elif checkout_status == 'success':
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking was saved successfuly.', category='alert-success')
            new_booking = None

    form = BookingForm()
    if form.validate_on_submit():

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide price ID you would like to charge
                    'price': form.time_period.data.api_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url= url_for('booking_views.dashboard', _external=True, checkout_status='success'),
            cancel_url= url_for('booking_views.dashboard', _external=True, checkout_status='canceled'),
            customer = current_user.stripe_id,
        )

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
            price_id = price_used.id,
            payment_intent = checkout_session.payment_intent,
        )

        return redirect(checkout_session.url)

    else:
        flash_errors(form)

    parkings = Parking.query.filter(Parking.scooters.any()).all()

    return render_template('dashboard.html', form=form, parkings=parkings,
                            page_name='dashboard', date_today=date.today(),
                            time_now=datetime.now().strftime("%H:00"))

@booking_views.route('/tickets', methods=['GET', 'POST'])
def tickets():
    form = TicketForm()
    if form.validate_on_submit():
        booking_chosen = Booking.query.get(form.booking_id.data)
        if form.refund.data:
            refund(booking_chosen.payment_intent)
            db.session.delete(booking_chosen)
            db.session.commit()

    return render_template('tickets.html', form=form, page_name='tickets', bookings=current_user.bookings)