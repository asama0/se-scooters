from app import db
from app.models import Scooter, Parking
import csv

with open('csv/scooters.csv', 'w', newline='') as file:
    csv_reader = csv.DictReader(file, delimiter=',')

    for line_count, row in enumerate(csv_reader):
        if line_count == 0:
            continue

        new_scooter_parking = Parking.query.filter(name=row['parking_name'])

        db.session.add(
            Scooter(parking_id=new_scooter_parking.id)
        )

    db.session.commit()