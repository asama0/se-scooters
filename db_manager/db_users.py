from app import db, bcrypt
from app.models import User
import stripe
import csv
from datetime import datetime


def add_users():
    with open('csv/users.csv', 'r', newline='') as file:
        csv_reader = csv.DictReader(file, delimiter=',')

        for row in csv_reader:

            hashedPassword = bcrypt.generate_password_hash(row['password']).decode('utf-8')
            new_stripe_id = stripe.Customer.create()['id']

            print(row['password'], '==', '5pbHUKESWV%O!', '?', bcrypt.check_password_hash(hashedPassword, '5pbHUKESWV%O!'))

            db.session.add(
                User(
                    name=row['name'], email=row['email'], password=hashedPassword,
                    birth_date=datetime.strptime(row['birth_date'], '%d/%m/%Y'),
                    phone=int(row['phone']), stripe_id=new_stripe_id,
                    privilege=int(row['privilege'])
                )
            )
            db.session.commit()