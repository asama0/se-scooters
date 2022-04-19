from flask.testing import FlaskClient
import json
from flask import url_for
from datetime import date

from app import app, db, models
from tests import client

def test_edit_profile(client:FlaskClient):
    # logging in as user
    response = client.post(
        '/login',
        data=json.dumps(dict(
            email='dkacubed+user@gmail.com', password='lslOWi@&ObQs',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    # checking if account page exists
    response = client.get('/account',follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == url_for('account')

    # trying to edit accout name, date of birth, phone number
    response = client.post(
        '/account',
        data=json.dumps(dict(
            name='peter pan', birth_date='1900-01-01',
            phone='123454321',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    user_user = models.User.query.get(3)

    assert user_user.name == 'peter pan'
    assert user_user.birth_date == date.fromisoformat('1900-01-01')
    assert user_user.phone == 123454321



