from flask import Blueprint, render_template, url_for, flash, redirect, request
from datetime import date, datetime, timedelta
import stripe
from telnetlib import Telnet

from app import db
from .views import current_user, login_required
from .models import *
from .forms import *
from stripe_functions import *
from helper_functions import *
from components.email_with_image import send_mail


booking_views = Blueprint('booking_views', __name__,
                          static_folder='static', template_folder='template')

new_booking:Booking = None


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

            price = Price.query.get(new_booking.price_id)

            send_mail(
                'Enjoy the ride!', current_user.email, 'reciept',
                payment_id=new_booking.id, payment_amount=price.amount ,
                payment_hours=price.get_timedelta().seconds//3600
                +24*price.get_timedelta().days,
                payment_discount=0, payment_total=price.amount,
                payemnt_date_created=new_booking.created_date_time
            )
            flash('Booking was saved successfuly.', category='alert-success')
            new_booking = None

    form = BookingForm()
    if form.validate_on_submit():
        discounts = None
        totalHours = 0
        weekAgo = datetime.today() - timedelta(days=7)
        senior = datetime.today() - timedelta(days=21900)

        # counts the booking hours in the last 7 days
        userBookings = Booking.query.filter_by(user_id=current_user.id).all()
        for booking in userBookings:
            if booking.created_date_time > weekAgo:
                if booking.price_id == 4:
                    totalHours += 1
                elif booking.price_id == 3:
                    totalHours += 4
                elif booking.price_id == 2:
                    totalHours += 24
                elif booking.price_id == 1:
                    totalHours += 168

        # applies the discount if the current user is a regular user or a senior citizen
        if totalHours > 7 or datetime.combine(current_user.birth_date, datetime.min.time()) < senior:
            discounts = [{'coupon': "returning", }]

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide price ID you would like to charge
                    'price': form.time_period.data.api_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            discounts=discounts,
            success_url=url_for('booking_views.dashboard',
                                _external=True, checkout_status='success'),
            cancel_url=url_for('booking_views.dashboard',
                               _external=True, checkout_status='canceled'),
            customer=current_user.stripe_id,
        )

        pickup_date = datetime.combine(
            form.pickup_date.data, form.pickup_time.data)
        scooter_chosen = Scooter.query.filter(
            (Scooter.availability == True) &
            (Scooter.parking_id == form.pickup_parking_id.data)
        ).first()
        price_used = form.time_period.data
        parking_id = form.pickup_parking_id.data

        new_booking = Booking(
            pickup_date=pickup_date,
            user_id=current_user.id,
            scooter_id=scooter_chosen.id,
            parking_id=parking_id,
            price_id=price_used.id,
            payment_intent=checkout_session.payment_intent,
        )

        return redirect(checkout_session.url)

    else:
        flash_errors(form)

    parkings = Parking.query.filter(Parking.scooters.any()).all()

    return render_template(
        'dashboard.html', form=form, parkings=parkings,
        not_available_times_form=NotAvailableTimesForm(),
        page_name='dashboard', date_today=date.today(),
        time_now=datetime.now().strftime("%H:00")
    )


@booking_views.route('/tickets', methods=['GET', 'POST'])
@login_required
def tickets():
    global new_booking

    form = TicketForm()
    if request.method == "POST":
        if form.validate_on_submit():
            booking_chosen:Booking = Booking.query.get(form.booking_id.data)

            if form.refund.data:
                refund(booking_chosen.payment_intent)
                db.session.delete(booking_chosen)
                db.session.commit()
            elif form.activate.data:
                with Telnet('192.168.217.174', 23) as tn:
                    tn.write(bytes(str(booking_chosen.scooter_id), 'utf-8'))
                    tn.close()
                return redirect(url_for('activate', token=str(booking_chosen.scooter_id)))
            elif form.extend.data:
                new_price:Price = Price.query.filter_by(lookup_key=form.new_dutration.data.lookup_key).first()
                pickup_date = booking_chosen.pickup_date
                scooter_chosen_id = booking_chosen.scooter_id


                refund(booking_chosen.payment_intent)
                db.session.delete(booking_chosen)
                db.session.commit()
                flash('Old booking was refunded', category='alert-success')

                checkout_session = stripe.checkout.Session.create(
                    line_items=[{'price': new_price.api_id, 'quantity': 1}],
                    mode='payment',
                    success_url=url_for('booking_views.dashboard',
                                        _external=True, checkout_status='success'),
                    cancel_url=url_for('booking_views.dashboard',
                                    _external=True, checkout_status='canceled'),
                    customer=current_user.stripe_id,
                )

                new_booking = Booking(
                    pickup_date=pickup_date,
                    user_id=current_user.id,
                    scooter_id=scooter_chosen_id,
                    parking_id=booking_chosen.parking_id,
                    price_id=new_price.id,
                    payment_intent=checkout_session.payment_intent,
                )

                return redirect(checkout_session.url)
        else:
            flash_errors(form)

    return render_template(
        'tickets.html', form=form, page_name='tickets',
        not_available_durations_form=NotAvailableDurationsForm(),
        bookings=current_user.bookings, Price=Price, Parking=Parking
    )
