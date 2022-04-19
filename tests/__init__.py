import pytest
import runpy

from app import app, db, models

# creating and configuring the app object
app.config['SECRET_KEY'] = 'WEKAS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = False
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

import db_manager

@pytest.fixture
def client():
    db.create_all()
    db_manager.add_users()
    db_manager.add_parkings()
    db_manager.add_scooters()
    db_manager.add_prices()

    with app.test_client() as client:
        print(models.User.query.all())
        yield client

    db.session.remove()
    db.drop_all()
