from app import db

db.create_all()

print('Database has been created!')

from db_manager.db_users import add_users
from db_manager.db_parkings import add_parkings
from db_manager.db_scooters import add_scooters
from db_manager.db_prices import add_prices

add_users()
add_parkings()
add_scooters()
add_prices()

print('Database entries have been added successfully!')