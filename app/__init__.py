from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# creating and configuring the app object
app = Flask(__name__)
# configure the app from config.py
app.config.from_object('config')



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
from app.booking_views import booking_views

app.register_blueprint(authentication_views)
app.register_blueprint(booking_views)


