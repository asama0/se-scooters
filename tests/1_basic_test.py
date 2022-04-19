from flask.testing import FlaskClient
import json
from flask import url_for

from app import app, db, models
from tests import client


def test_test(client):
    assert 1+1 == 2


def test_index(client:FlaskClient):
    response = client.get('/')
    assert response.status_code == 200