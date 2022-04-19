from flask.testing import FlaskClient
import json
from flask import url_for

from app import app, db, models
from tests import client


def test_login(client:FlaskClient):
    #checking if login page exists
    response = client.get('/login')
    assert response.status_code == 200

    # testing successfull admin login
    response = client.post(
        '/login',
        data=json.dumps(dict(
            email='dkacubed+admin@gmail.com', password='5pbHUKESWV%O!',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    # chacking if login was successful and we've been redirected to dashboard
    assert response.status_code == 200
    assert response.request.path == url_for('booking_views.dashboard')
