from app import db
from app.models import Price
from stripe_functions import get_all_prices

for price in get_all_prices():

    db.session.add(
        Price(
            api_id=price['api_id'],
            lookup_key=price['lookup_key'],
            amount=price['amount']
        )
    )

db.session.commit()