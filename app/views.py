
from flask import render_template,url_for,flash, redirect,request
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from flask_login import login_user
from .forms import registrationForm, loginForm
from flask_login import login_user,current_user,login_required,logout_user
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from app import app, db, admin
from .models import *

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# add models to admin page
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Scooter, db.session))
admin.add_view(ModelView(Parking, db.session))
admin.add_view(ModelView(Cost, db.session))

@app.route('/')
@app.route('/index')
def index():
    

    return render_template('index.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
    #if current_user.is_authenticated:
        #return redirect(url_for('index'))
    form = registrationForm()
    if form.validate_on_submit():
        hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name = form.name.data, email= form.email.data, password = hashedPassword,birth_date=datetime.utcnow(),phone=44498989646)
        db.session.add(user)
        db.session.commit()
        flash('account created')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated:
       # return redirect(url_for('index'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                next = request.args.get('next')
                return redirect(next) if next else redirect(url_for('/'))
            flash('faild')
    return render_template('login.html', title='login', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('login.html', title='login')
