import stripe
from flask import redirect
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

get_discount(id)
returns the percentage off, amount off, and the number of times this discount have been used

checkout(app, domain, price, discountID)
creates a checkout session with app: current app, domain: the current domain, price: price lookup, discountID: discount id or None, returns True if successful
"""



# ***: VERY GOOD AND CLEAN CODE WITH HELPFUL COMMENTS.


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
    # !!!: "id" MUST BE REPLASED WITH id RIGHT?
    stripe.Product.modify("id", unit_amount = int(newPrice * 100))



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
    return float(stripe.Price.list(lookup_keys=[lookUpKey],).get("data")[0].get("unit_amount")) / 100



# returns the price id using priceLookUpKey (the price lookup key)
def get_price_id(priceLookupKey):
    return stripe.Price.list(lookup_keys=[priceLookupKey]).get("data")[0].get("id")



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



# creates a checkout session with app: current app, domain: the current domain, price: price lookup, discountID: discount id or None, returns True if successful
def checkout(app, domain, price, discountID):

    # ???: I THINK THIS PART NEEDS TO BE IN SERVER.PY AND GETS PRICE, discountID
    # ???: FROM AN HTML FROM. TRY ADDING A BOOKING FROM A FORM.
    # creates a checkout session
    @app.route('/create-checkout-session', methods=['POST'])
    def create_checkout_session():
        try:

            # applies the discount if discountID is not None
            if discountID:
                checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            # Provide price ID you would like to charge
                            'price': get_price_id(price),
                            'quantity': 1,
                        },
                    ],
                    mode='payment',
                    discounts=[{'coupon': discountID,}],
                    success_url=domain + '/success.html',
                    cancel_url=domain + '/cancel.html',
                )
            # proceeds without a discount if discountID is None
            else:
                checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            # Provide price ID you would like to charge
                            'price': get_price_id(price),
                            'quantity': 1,
                        },
                    ],
                    mode='payment',
                    success_url=domain + '/success.html',
                    cancel_url=domain + '/cancel.html',
                )

        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)

    return False





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
