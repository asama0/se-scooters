from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY']= 'WEKAS '

from app import views
from .auth import auth
    
