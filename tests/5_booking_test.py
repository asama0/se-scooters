from flask.testing import FlaskClient
import json
from flask import url_for
from sqlalchemy.inspection import inspect

from app import app, db, models
from tests import client

def test_booking(client:FlaskClient):
    # logging in as admin
    response = client.post(
        '/login',
        data=json.dumps(dict(
            email='dkacubed+admin@gmail.com', password='5pbHUKESWV%O',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    response = client.get('/admin/',follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/admin/'

    response = client.post(
        '/admin/',
        data=json.dumps(dict(
            user_email='dkacubed+admin@gmail.com', pickup_date='2000-01-01',
            pickup_time='04:00', time_period='1', scooter_id='3',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    assert models.Booking.query.filter_by(user_id=1).all()