from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

# creating and configuring the app object
app = Flask(__name__)
# configure the app from config.py
app.config.from_object('config')


# creating the database object
db = SQLAlchemy(app)

# admin pages setup
admin = Admin(app, template_mode='bootstrap4')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# combine code from all other files to this file
from app import views, models
