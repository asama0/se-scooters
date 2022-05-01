# How to setup

## UoL computer labs setup:
```shell
cd ~
module add anaconda3
python3 -m venv flask
source flask/bin/activate
flask/bin/pip install flask flask-login flask-mail flask-sqlalchemy flask-migrate flask-whooshalchemy flask-wtf flask-babel coverage flask-admin flask-bcrypt email_validator WTForms-SQLAlchemy stripe jwt numpy python-dateutil pytest
```
For other OS plese visit the "How to setup Flask" section in the wiki.

# How to Run

## Adding database entries (make sure app.db file dosen't exist):
```shell
python3 -m db_manager
```

## Run flask:
```shell
source ~/flask/bin/activate ### (If in UoL computer Lab) ###
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

# Card to test with (use any random CVC and any future date):

## 4242424242424242 Visa
## 01632 960231 Phone if needed (fakenumber.org/united-kingdom)
