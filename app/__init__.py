from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating and configuring the app object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'WEKAS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app.db'

# creating the database object
db = SQLAlchemy(app)

# combine code from all other files to this file
from app import views, models