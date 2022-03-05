
from flask import render_template, url_for, flash, redirect, request, abort
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from flask_login import login_user, current_user, login_required, logout_user
from flask_bcrypt import Bcrypt
from urllib.parse import urlparse, urljoin

from app import app, db, admin, login_manager
from .models import *
from .forms import *


bcrypt = Bcrypt(app)


# this is for flask login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# add models to admin page
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Scooter, db.session))
admin.add_view(ModelView(Parking, db.session))
admin.add_view(ModelView(Cost, db.session))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


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
        flash(f'user {user.email} was created')
        return redirect(url_for('login'))

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
                flash('Logged in successfully.')

                next = request.args.get('next')
                if not is_safe_url(next):
                    return abort(400)

                return redirect(next or url_for('dashboard'))
            flash('Log in failed.')

    return render_template('login.html', title='login', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# check if url in get request is safe
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
