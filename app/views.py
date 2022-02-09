
from flask import render_template,url_for,flash, redirect
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from flask_login import login_user
from .forms import registrationForm, loginForm
from flask_login import login_user,current_user,login_required
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from app import app, db, admin
from .models import *

bcrypt = Bcrypt(app)
login_manager = LoginManager()

# add models to admin page
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Scooter, db.session))
admin.add_view(ModelView(Parking, db.session))
admin.add_view(ModelView(Cost, db.session))

@app.route('/')
def index():

    return render_template('index.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registrationForm()
    if form.validate_on_submit():
        hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name = form.name.data, email= form.email.data, password = hashedPassword,birth_date=datetime.utcnow(),phone=44498989)
        db.session.add(user)
        db.session.commit()
        flash('account created')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return  redirect(url_for('home'))
        else:
            flash('faild')
    return render_template('login.html', title='login', form=form)


