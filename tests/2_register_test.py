from flask.testing import FlaskClient
import json
from flask import url_for

from app import app, db, models
from tests import client


def test_register(client:FlaskClient):
    # checking if register page exists
    response = client.get('/register')
    assert response.status_code == 200

    # testing SUCCESSFUL registeration
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

    # testing FAILED registeration (wrong phone number)
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


