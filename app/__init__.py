from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_login import login_manager


# creating and configuring the app object
app = Flask(__name__)
# configure the app from config.py
app.config.from_object('config')


# creating the database object
db = SQLAlchemy(app)

# admin pages setup
admin = Admin(app, template_mode='bootstrap4')



# combine code from all other files to this file
from app import views, models