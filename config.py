import os

# path to base directory
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'WEKAS'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
