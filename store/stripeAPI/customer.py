from . import stripe

def create_customer(user):
    customer = stripe.Customer.create(
        description=user.description,
        email=user.email,
        name=user.get_full_name()

    )
    return customer