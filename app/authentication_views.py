from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, login_required, logout_user
import stripe
from app import db, login_manager, bcrypt

from .views import current_user
from .models import *
from .forms import *
from stripe_functions import *
from helper_functions import *
from components.email_with_image import send_mail

authentication_views = Blueprint('authentication_views', __name__, static_folder='static', template_folder='template')

# this is for flask login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@authentication_views.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('booking_views.dashboard'))

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
        return redirect(url_for('authentication_views.login'))
    else:
        flash_errors(form)

    return render_template('register.html', title='register', form=form)

@authentication_views.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('booking_views.dashboard'))

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

                return redirect(next or url_for('booking_views.dashboard'))
            flash('Log in failed.', category='alert-danger')
    else:
        flash_errors(form)

    return render_template('login.html', title='login', form=form)

@authentication_views.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', category='alert-success')
    return redirect(url_for('authentication_views.login'))

#here user requist password reset by submmiting email account, email must be registerd
@authentication_views.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('booking_views.dashboard'))
    form = forgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        reset_email(user)
        return redirect(url_for('authentication_views.login'))
    return render_template('forgotPassword.html', title='Forgot Password', form=form)


#here user will write the new paassword after clicking on the link recieved in the email
@authentication_views.route("/forgot_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('booking_views.dashboard'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Token was not verified')
        return redirect(url_for('index'))
    form = resetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        return redirect(url_for('authentication_views.login'))
    return render_template('resetPassword.html', title='Reset Password', form=form)

# the reset password email sender
# email is visable for now, must be hidden for security reasons
def reset_email(user):
    token = user.get_reset_token()
    send_mail("Password reset", user.email, 'forgetpassword', forgot_password_url=url_for('authentication_views.reset_token', token=token, _external=True))







