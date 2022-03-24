import email
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import current_user, login_required
from email.message import EmailMessage
import smtplib
from datetime import datetime, date
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
    title = "Edit Profile"
    
    form = editProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.phone = form.phone.data
        current_user.birth_date = form.birth_date.data
        
        db.session.commit()
        flash("Updated Successfully!", category='alert-success')
    else:
        flash_errors(form)
    return render_template('account.html', page_name='account',form=form)

@app.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    form = feedbackForm()
    urgent = False
    feedbackText = ""

    # retrieve the data 
    if form.validate_on_submit():
        feedbackText += "Feedback submitted on " + date.today().strftime("%B %d, %Y") + "\n"
        feedbackText += "Name: " + current_user.name + "\n"
        feedbackText += "Email: " + current_user.email + "\n"
        feedbackText += "Overall eexperience: " + form.experience.data + "\n\n"
        feedbackText += "Comments: \n" + form.feedback.data
        urgent = form.urgent.data

        msg = EmailMessage()
        msg.set_content(feedbackText)

        
        msg['From'] = "dkacubed@gmail.com"
        msg['To'] = "dkacubed@gmail.com"
        if urgent:
            msg['Priority'] = '2'
            msg['Subject'] = 'URGENT feedback'
        else:
            msg['Priority'] = '0'
            msg['Subject'] = 'feedback'
        

        # send the feedback email 
        try:
            smtp_server = smtplib.SMTP("smtp.gmail.com:587")
            smtp_server.starttls()
            smtp_server.login("dkacubed@gmail.com", "RX52@h@MqMj3")
            smtp_server.send_message(msg)
            smtp_server.close()
            flash('Feedback submitted successfuly.')
            print ("Email sent successfully")
        except Exception as ex:
            print ("Failed to send the email",ex)
    else:
        flash_errors(form)


    return render_template('feedback.html', page_name='feedback', form=form)




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

