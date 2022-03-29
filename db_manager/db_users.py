from app import db, bcrypt
from app.models import User
import stripe
import csv
from datetime import datetime

with open('csv/users.csv', 'w', newline='') as file:
    csv_reader = csv.DictReader(file, delimiter=',')

    for line_count, row in enumerate(csv_reader):
        if line_count == 0:
            continue

        hashedPassword = bcrypt.generate_password_hash(row['password']).decode('utf-8')
        new_stripe_id = stripe.Customer.create()['id']

        db.session.add(
            User(
                name=row['name'], email=row['email'], password=hashedPassword,
                birth_date=datetime.strptime(row['birth_date'], '%d/%m/%Y'),
                phone=int(row['phone']), stripe_id=new_stripe_id,
                privilege=int(row['privilege'])
            )
        )

    db.session.commit()