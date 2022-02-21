#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask
import stripeFunctions as SF
import stripe


app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'


SF.checkout(app, YOUR_DOMAIN, "1h", "returning")


if __name__ == '__main__':
    app.run(port=4242)