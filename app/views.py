
from crypt import methods
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, login_required, logout_user
from urllib.parse import urlparse, urljoin
from sqlalchemy import and_
from datetime import datetime

from app import app, db, login_manager, bcrypt
from .models import *
from .forms import *
from stripe_functions import *

booking_form:BookingForm

# check if url in get request is safe
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), category='alert-danger')

# this is for flask login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


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
        (Scooter.parking_id==booking_form.pickup_location.data.id)).first()
        print(f'{scooter_chosen = }')
        print(f'{booking_form.pickup_location.data.id = }')
        price_used = booking_form.time_period.data

        new_booking = Booking(
            pickup_date= pickup_date,
            user_id = current_user.id,
            scooter_id = scooter_chosen.id,
            price_id = price_used.id
        )

        db.session.add(new_booking)
        db.session.commit()
        scooter_chosen.parking_id = None
        scooter_chosen.availability = False
        booking_form = None # form data won't be used any more
        flash('Booking was saved successfuly.')


    form = BookingForm()
    if form.validate_on_submit():
        booking_form = form
        return redirect(url_for('checkout', _method='POST'), code=307)
    else:
        flash_errors(form)

    return render_template('dashboard.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = registrationForm()
    if form.validate_on_submit():
        hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data,
                    password=hashedPassword, birth_date=form.birth_date.data, phone=form.phone.data)
        db.session.add(user)
        db.session.commit()
        flash(f'user {user.email} was created', category='alert-success')
        return redirect(url_for('login'))
    else:
        flash_errors(form)

    return render_template('register.html', title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Logged in successfully.', category='alert-success')

                next = request.args.get('next')
                if not is_safe_url(next):
                    return abort(400)

                return redirect(next or url_for('dashboard'))
            flash('Log in failed.', category='alert-danger')
    else:
        flash_errors(form)

    return render_template('login.html', title='login', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', category='alert-success')
    return redirect(url_for('login'))


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
    )

    return redirect(checkout_session.url)
