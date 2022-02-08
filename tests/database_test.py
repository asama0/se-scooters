import os
import sys
import pytest
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# getting the name of the directory where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from app import app, db, models

@pytest.fixture
def client():
    # path to base directory
    # basedir = os.path.abspath(os.path.dirname(__file__))

    # creating and configuring the app object
    app.config['SECRET_KEY'] = 'WEKAS'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['TESTING'] = True

    with app.test_client() as client:
        db.create_all()
        yield client

    db.session.remove()
    db.drop_all()

def test_adding_user(client):
    pass