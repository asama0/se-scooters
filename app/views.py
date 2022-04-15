from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import current_user, login_required
from app import app, db

from .models import *
from .forms import *
from stripe_functions import *
from helper_functions import *
from analytics_quries import *


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@login_required
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

@login_required
@app.route('/account', methods=['GET', 'POST'])
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
    return render_template('account.html', page_name='account',form=form)

@login_required
@app.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    form = feedbackForm()

    # retrieve the feedback then adds it to the database 
    if form.validate_on_submit():
        feedback = Feedback(experience=form.experience.data, feedback=form.feedback.data)
        db.session.add(feedback)
        db.session.commit()
        flash('Feedback submitted successfully')

    return render_template('feedback.html', page_name='feedback', form=form)


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
    return render_template('analytics_index.html')

