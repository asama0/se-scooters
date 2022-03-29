import stripe
from datetime import datetime
from time import mktime

stripe.api_key = "sk_test_51KRcJeAWMfIxY0DOsedfn3ItYh6VF1h7yq7lWt3EoGCOCmvCUOgHRbglgaHr5izKL6LS1zSUnMOOYuoB7IjBgT6H00xY6mZPuL"
# DO *NOT* SHARE THE API KEY

"""
the id for the product scooter:
prod_L7tv4Gbl7YQuKm


prices:
lookup key | ID
1h         | price_1KS0sAAWMfIxY0DOOfJJlzag
4h         | rice_1KS0sAAWMfIxY0DOXu2iK9M6
1d         | price_1KS0sAAWMfIxY0DO2wKYA9OY
1w         | price_1KS0sBAWMfIxY0DOyf4iumx9

discounts:
returning


the list of functions:

create_a_price(id, price, lookupKey)
creates a price for the product id, with the price which can be obtained using lookupKey

create_a_discount(id, percentageOff, amountOff)
creates  discount with the given id and applies the amount amountOff or percentage (0-100) percentageOff, provide one while the other is None

edit_price(id, newPrice)
edits the price id to the new price newprice (the id of the price not the product)

edit_discount(id, newPercentageOff, newAmountOff)
edit the discount to the new percentage off and amount off (one of them must equal to None)

get_price(lookUpKey)
returns the price from its lookup key

get_price_id(priceLookupKey)
returns the price id using priceLookUpKey (the price lookup key)

get_price_info(priceLookupKey)
returns the price id and amount using priceLookUpKey (the price lookup key)

get_all_prices()
returns a list of all the prices, each with its lookup key, Id, and amount

get_discount(id)
returns the percentage off, amount off, and the number of times this discount have been used

checkout(app, domain, price, discountID)
creates a checkout session with app: current app, domain: the current domain, price: price lookup, discountID: discount id or None, returns True if successful
"""

# creates a price for the product id, with the price which can be obtained using lookupKey
def create_a_price(id, price, lookupKey):
    stripe.Price.create( product = id, unit_amount = int(price * 100), currency = "GBP", lookup_key = lookupKey,)


# creates  discount with the given id and applies the amount amountOff or percentage (0-100) percentageOff, provide one while the other is None
def create_a_discount(id, percentageOff, amountOff):
    if percentageOff and (not amountOff):
        stripe.Coupon.create(duration = "once", id = id, percent_off = int(percentageOff), currency="GBP")
    elif amountOff and (not percentageOff):
        stripe.Coupon.create(duration = "once", id = id, currency="GBP", amount_off = int(amountOff * 100))


# edits the price to the new price newprice (the id of the price not the product)
def edit_price(id, newPrice):
    stripe.Product.modify(id, unit_amount = int(newPrice * 100))


# edit the discount to the new percentage off and amount off (one of them must equal to None)
def edit_discount(id, newPercentageOff, newAmountOff):

    # deletes the old discount object
    stripe.Coupon.delete(id)

    # creates a new discount object with the new values
    if newPercentageOff and (not newAmountOff):
        stripe.Coupon.create(duration = "once", id = id, percent_off = int(newPercentageOff), currency="GBP")
    elif newAmountOff and (not newPercentageOff):
        stripe.Coupon.create(duration = "once", id = id, currency="GBP", amount_off = int(newAmountOff * 100))


# returns the price from its lookup key
def get_price(lookUpKey):
    return float(stripe.Price.list(lookup_keys=[lookUpKey]).get("data")[0].get("unit_amount")) / 100


# returns the price id using priceLookUpKey (the price lookup key)
def get_price_id(priceLookupKey):
    return stripe.Price.list(lookup_keys=[priceLookupKey]).get("data")[0].get("id")


# returns the price id and amount using priceLookUpKey (the price lookup key)
def get_price_info(priceLookupKey):
    return stripe.Price.list(lookup_keys=[priceLookupKey]).get("data")[0].get("id"), (float(stripe.Price.list(lookup_keys=[priceLookupKey]).get("data")[0].get("unit_amount"))/100)


# returns a list of all the prices, each with its lookup key, Id, and amount
def get_all_prices():

    fullList = stripe.Price.list(active=True)
    specificList = []

    for price in fullList:
        specificList.append(
            {
               'api_id': price.get("id"),
               'lookup_key': price.get("lookup_key"),
               'amount': float(price.get("unit_amount"))/100
            }
        )

    return specificList


# returns the percentage off, amount off, and the number of times this discount have been used
def get_discount(id):

    # retrieves the discount
    discountData = stripe.Coupon.retrieve(id)
    percentage = int(discountData.get("percent_off"))
    amount = None
    used = discountData.get("times_redeemed")

    # seperately assigns the amount off to avoid errors
    if discountData.get("amount_off"):
        amount = float(discountData.get("amount_off")) / 100

    return [percentage, amount, used]


def list_payments(start_date:datetime, end_date:datetime):
    start_unix_timestamp = mktime(start_date.timetuple())
    end_unix_timestamp = mktime(end_date.timetuple())

    return stripe.PaymentIntent.list(created={
        'gte': start_unix_timestamp, 'lte': end_unix_timestamp
    })

def refund(payment_intent):
    stripe.Refund.create(payment_intent=payment_intent)

# print(get_all_prices())
#create_a_price("prod_L7tv4Gbl7YQuKm", 10, "1h")
#create_a_price("prod_L7tv4Gbl7YQuKm", 40, "4h")
#create_a_price("prod_L7tv4Gbl7YQuKm", 80, "1d")
#create_a_price("prod_L7tv4Gbl7YQuKm", 500, "1w")

#print(str(get_price("1h")))
#print(str(get_price("4h")))
#print(str(get_price("1d")))
#print(str(get_price("1w")))

#print(str(get_price_id("1h")))

#create_a_discount("test", 0, 3)
#edit_discount("test", 20, None)
#print(get_discount("test"))
#stripe.Coupon.delete("test")

#create_a_discount("returning", 10, None)
#print(get_discount("returning"))

#get_all_prices()
