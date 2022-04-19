from flask.testing import FlaskClient
import json
from flask import url_for

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

    # checking if feedback page exists
    response = client.get('/feedback',follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == url_for('feedback')

    # trying to send a feedback
    response = client.post(
        '/feedback',
        data=json.dumps(dict(
            experience='average', feedback='Best website!',
        )),
        content_type='application/json',
        follow_redirects=True,
    )

    the_feedback = models.Feedback.query.get(1)
    assert the_feedback.experience == 'average'
    assert the_feedback.feedback == 'Best website!'