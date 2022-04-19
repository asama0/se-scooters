from app import db
from app.models import Scooter, Parking
import csv


def add_scooters():
    with open('csv/scooters.csv', 'r', newline='') as file:
        csv_reader = csv.DictReader(file, delimiter=',')

        for row in csv_reader:

            new_scooter_parking = Parking.query.filter_by(name=row['parking_name']).first()

            db.session.add(
                Scooter(parking_id=new_scooter_parking.id)
            )

        db.session.commit()