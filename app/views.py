from flask import render_template

from app import app, db
from .models import *

@app.route('/')
def index():
    return render_template('index.html')