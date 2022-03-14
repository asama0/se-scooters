import numpy as np
import dateutil.relativedelta
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import login_user, current_user, login_required, logout_user
from urllib.parse import urlparse, urljoin
from datetime import datetime, timedelta
import stripe
from flask_mail import Message
from app import app, db, login_manager, bcrypt, mail

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

def query_booking_by_date(start_date, end_date):
    # querying bookings from database
    result_query = Booking.query \
        .filter(and_(Booking.date >= start_date, Booking.date <= end_date)) \
        .order_by(Booking.date) \
        .all()

    # change every booking to a dictionary
    result_dict = [
        {'date': str(booking.date),
         'amount': booking.amount,
         'duration': booking.duration}
        for booking in result_query
    ]

    return result_dict


# for _ in range(20):
#     db.session.add(Booking(
#         amount=random.randrange(1,200) + random.random(),
#         date=datetime(
#             random.randrange(1980,2021),
#             random.randrange(1,12),
#             random.randrange(1,28),
#             random.randrange(0,23),
#             random.randrange(0,23),
#             random.randrange(0,59),
#             random.randrange(0,59)
#             ),
#         duration=random.randrange(1,4),
#         )
#     )
#
# db.session.commit()

# pprint(query_booking_by_date(datetime(1980, 1, 1), datetime(2021, 12, 31)))

# pprint(query_booking_by_date(datetime(2015, 1, 1), datetime(2015, 12, 31)))


# qu = query_booking_by_date(datetime(2000, 1, 1), datetime(2015, 12, 31))
# print(qu[0]["amount"])
# print(qu)


# ---------------------------------------------------------#

start_year = int(datetime.today().strftime('%Y'))
start_month = int((datetime.today().strftime('%m')))
start_day = int((datetime.today().strftime('%d')))


def get_full_data():
    resssult = Booking.query.filter(and_(Booking.id >= 1, Booking.date <= datetime(start_year, start_month, start_day)))

    # change every booking to a dictionary
    result_dict = [
        {'date': str(booking.date),
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
            (datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(
                days=period_list_start)),
            datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(days=period_list_end))
    elif period_key == "month":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(
                days=period_list_start)),
            datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(days=period_list_end))
    elif period_key == "year":
        period = query_booking_by_date(
            (datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(
                months=period_list_start)),
            datetime(start_year, start_month, start_day) - dateutil.relativedelta.relativedelta(months=period_list_end))
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
# one week graph
get_analitics(7, "week")
# one month graph
get_analitics(30, "month")
# one year graph
get_analitics(12, "year")
# general dynamic graph
get_data_list_days(1, 1, "total")


# sending array to javascript
@app.route('/week_request', methods=['POST'])
def post_week_request():
    # return a list of integers
    return jsonify(week)


@app.route('/month_request', methods=['POST'])
def post_month_request():
    # return a list of integers
    return jsonify(month)


@app.route('/year_request', methods=['POST'])
def post_year_request():
    # return a list of integers
    return jsonify(year)


@app.route('/total_request', methods=['POST'])
def post_total_request():
    # return a list of integers
    return jsonify(max_period)

@app.route('/home')
def home():
    return render_template('home_page.html')

@app.route('/home-admin')
def home_admin():
    return render_template('home_admin.html')
# the reset password email sender
# email is visable for now, must be hidden for security reasons
def reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request',
                   sender='salimbader734@gmail.com',
                   recipients=[user.email])
    message.body = f''' visit the following link to reset your password:
{url_for('reset_token', token=token, _external=True)}
'''
    mail.send( message)

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
        new_stripe_id = stripe.Customer.create()['id']
        user = User(name=form.name.data, email=form.email.data,
                    password=hashedPassword, birth_date=form.birth_date.data,
                    phone=form.phone.data, stripe_id=new_stripe_id)
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
        customer = current_user.stripe_id,
    )

    return redirect(checkout_session.url)

#here user requist password reset by submmiting email account, email must be registerd
@app.route("/forgot_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = forgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        reset_email(user)
        return redirect(url_for('login'))
    return render_template('forgotPassword.html', title='Forgot Password', form=form)


#here user will write the new paassword after clicking on the link recieved in the email
@app.route("/forgot_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    user = User.verify_reset_token(token)
    if user is None:
        return redirect(url_for('forgotPassword'))
    form = resetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('resetPassword.html', title='Reset Password', form=form)

