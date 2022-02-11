
from flask import render_template, request
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

@app.route('/postmethod', methods = ['POST'])
def post_javascript_data():
    jsdata = request.form['javascript_data']
    print(jsdata)
    return jsdata

count_requests = 0
@app.route('/requestdata', methods = ['POST'])
def post_request_data():
    global count_requests # saying that count_requests is a global variable
    count_requests += 1
    return f"this is the request {count_requests}"
