from crypt import methods
from flask import render_template
from flask_admin.contrib.sqla import ModelView
from datetime import datetime

from app import app, db, admin
from .models import *

# add models to admin page
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Scooter, db.session))
admin.add_view(ModelView(Parking, db.session))
admin.add_view(ModelView(Cost, db.session))

@app.route('/')
def index():

    return render_template('index.html')

