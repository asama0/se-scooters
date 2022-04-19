from flask.testing import FlaskClient
import json
from flask import url_for

from app import app, db, models
from tests import client


def test_login(client:FlaskClient):
    # checking if login page exists
    response = client.get('/login')
    assert response.status_code == 200

    # testing SUCCESSFUL admin login
    response = client.post(
        '/login',
        data=json.dumps(dict(
            email='dkacubed+admin@gmail.com', password='5pbHUKESWV%O',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    # chacking if login was successful and we've been redirected to dashboard
    assert response.status_code == 200
    assert response.request.path == url_for('booking_views.dashboard')

    # LOGGING OUT
    response = client.get('/logout')

    # testing FAILED login (wrong password)
    response = client.post(
        '/login',
        data=json.dumps(dict(
            email='dkacubed+admin@gmail.com', password='abc123',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    # chacking if login was successful and we've been redirected to dashboard
    assert response.status_code == 200
    assert response.request.path == url_for('authentication_views.login')