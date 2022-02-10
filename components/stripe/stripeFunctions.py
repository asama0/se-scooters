import stripe
stripe.api_key = "sk_test_51KRcJeAWMfIxY0DOsedfn3ItYh6VF1h7yq7lWt3EoGCOCmvCUOgHRbglgaHr5izKL6LS1zSUnMOOYuoB7IjBgT6H00xY6mZPuL"
# DO *NOT* SHARE THE API KEY

"""
the id for the product scooter:
prod_L7tv4Gbl7YQuKm


the list of functions:

create_a_price(id, price, lookupKey)
creates a price for the product id, with the price which can be obtained using lookupKey

edit_price(id, newPrice)
edits the price id to the new price newprice (the id of the price not the product)

get_price(lookUpKey)
returns the price from its lookup key
"""






# creates a price for the product id, with the price which can be obtained using lookupKey
def create_a_price(id, price, lookupKey):
    stripe.Price.create(
    product = id,
    unit_amount = (price * 100),
    currency = "GBP",
    lookup_key = lookupKey,
    )


# edits the price id to the new price newprice (the id of the price not the product)
def edit_price(id, newPrice):
    stripe.Product.modify("id", unit_amount = "Updated Price")


# returns the price from its lookup key
def get_price(lookUpKey):
    return float(stripe.Price.list(lookup_keys=[lookUpKey],).get("data")[0].get("unit_amount")) / 100
    







#create_a_price("prod_L7tv4Gbl7YQuKm", 10, "test_price")

#print(str(get_price("test_price")))