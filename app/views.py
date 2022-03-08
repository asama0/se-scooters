
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, login_required, logout_user
from urllib.parse import urlparse, urljoin

from app import app, db, login_manager, bcrypt
from .models import *
from .forms import *
from .stripe_functions import *

from datetime import datetime

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


@app.route('/dashboard')
@login_required
def dashboard():
    form = BookingForm()
    if form.validate_on_submit():
        pass
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


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide price ID you would like to charge
                'price': get_price_id(price),
                'quantity': 1,
            },
        ],
        mode='payment',
        discounts=[{'coupon': discountID,}] if discountID else [],
        success_url= 'success',
        cancel_url= 'cancel',
    )

    if checkout_session.url == 'success':
        flash('Payment failed', category='alert-danger')
    else:
        flash('Payment failed', category='alert-success')

    return redirect(request.referrer, code=303)
