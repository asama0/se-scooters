from app import db

db.create_all()

print('Database has been created!')

from db_manager import db_users
from db_manager import db_parkings
from db_manager import db_scooters

print('Database entries have been added successfully!')