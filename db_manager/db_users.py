from app import db, bcrypt
from app.models import User
import stripe
import csv

with open('csv/users.csv', 'w', newline='') as file:
    csv_reader = csv.DictReader(file, delimiter=',')

    for line_count, row in enumerate(csv_reader):
        if line_count == 0:
            continue

        hashedPassword = bcrypt.generate_password_hash(row['password']).decode('utf-8')
        new_stripe_id = stripe.Customer.create()['id']
        new_user = User(name=row['name'], email=row['email'],
                    password=hashedPassword, birth_date=row['birth_date'],
                    phone=row['phone'], stripe_id=new_stripe_id,
                    privilege=row['privilege']
                )

        db.session.add(new_user)

    db.session.commit()