from flask.testing import FlaskClient
from flask import url_for
from pprint import pprint
import os
import sys
import pytest
import json

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
    app.config['WTF_CSRF_ENABLED'] = False

    app.config['TESTING'] = True

    with app.test_client() as client:
        db.create_all()
        yield client

    db.session.remove()
    db.drop_all()


def test_test(client):
    assert 1+1 == 2


def test_index(client:FlaskClient):
    response = client.get('/')
    assert response.status_code == 200


def test_register(client:FlaskClient):
    response = client.get('/register')
    assert response.status_code == 200

    # testing successfull registeration
    response = client.post(
        '/register',
        data=json.dumps(dict(
            name='tester', email='test@test.com', password='helloWorld!',
            password2='helloWorld!', birth_date='2000-01-01', phone='92445252',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == url_for('authentication_views.login')

    # testing failed registeration (wrong phone number)
    response = client.post(
        '/register',
        data=json.dumps(dict(
            name='tester', email='test@test.com', password='helloWorld!',
            password2='helloWorld!', birth_date='2000-01-01', phone='92445252asf',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == url_for('authentication_views.register')


def test_login(client:FlaskClient):
    response = client.get('/login')
    assert response.status_code == 200

    # testing successfull registeration
    response = client.post(
        '/register',
        data=json.dumps(dict(
            name='tester', email='test@test.com', password='helloWorld!',
            password2='helloWorld!', birth_date='2000-01-01', phone='92445252',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == url_for('authentication_views.login')

    # testing successfull login
    response = client.post(
        '/login',
        data=json.dumps(dict(
            email='test@test.com', password='helloWorld!',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == url_for('booking_views.dashboard')

    # uncomment to print users in database
    # print(models.User.query.all())
    # assert 3==2
