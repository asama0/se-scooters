from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

# creating and configuring the app object
app = Flask(__name__)
# configure the app from config.py
app.config.from_object('config')
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'salimbader734@gmail.com'
app.config['MAIL_PASSWORD'] = '123456SS'
mail = Mail(app)



# creating the database object
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'authentication_views.login'

# combine code from all other files to this file
from app import views
from app import models
from app import admin_views

# adding blueprints
from app.authentication_views import authentication_views

app.register_blueprint(authentication_views)



