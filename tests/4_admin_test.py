from flask.testing import FlaskClient
import json
from flask import url_for

from app import app, db, models
from tests import client

def test_admin(client:FlaskClient):
    # checking if admin page can be access without login
    response = client.get('/admin')
    assert response.status_code == 200
    assert response.request.path == url_for('authentication_views.login')

    # checking if user can access login
    response = client.post(
        '/login',
        data=json.dumps(dict(
            email='dkacubed+user@gmail.com', password='abc123',
        )),
        content_type='application/json',
        follow_redirects=True,
    )