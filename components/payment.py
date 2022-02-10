import Stripe

stripe.api_key = "sk_test_51KRcJeAWMfIxY0DOsedfn3ItYh6VF1h7yq7lWt3EoGCOCmvCUOgHRbglgaHr5izKL6LS1zSUnMOOYuoB7IjBgT6H00xY6mZPuL"

stripe.Customer.create(description = "My First Test Customer")

stripe.PaymentIntent.create(
  customer = '{{CUSTOMER_ID}}',
  currency = "usd",
  amount = 10,
  payment_method_types = ["card"],
  setup_future_usage = "on_session",
)



