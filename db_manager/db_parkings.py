from app import db
from app.models import Parking
import csv

with open('csv/parkings.csv', 'r', newline='') as file:
    csv_reader = csv.DictReader(file, delimiter=',')

    for line_count, row in enumerate(csv_reader):

        db.session.add(
            Parking(
                name=row['name'],
                latitude=float(row['latitude']),
                longitude=float(row['longitude'])
            )
        )

    db.session.commit()