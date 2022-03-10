import os
from flask import Flask, redirect
import stripe_functions as SF
import stripe


app = Flask(__name__,
            static_url_path='',
            static_folder='public')

domain = 'http://localhost:4242'
price = "4 hours"
discountID = "returning"

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:

        # applies the discount if discountID is not None
        if discountID:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide price ID you would like to charge
                        'price': SF.get_price_id(price),
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
                        'price': SF.get_price_id(price),
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




if __name__ == '__main__':
    app.run(port=4242)