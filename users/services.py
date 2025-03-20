import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    product_name = (f"{instance.course}" if instance.course else f"{instance.lesson}")
    product = stripe.Product.create(name=f"{product_name}")
    return product


def create_stripe_price(amount, product_id, currency="rub"):
    price = stripe.Price.create(
        unit_amount=int(amount * 100),
        currency=currency,
        product=product_id,
    )
    return price


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )

    return session.get("id"), session.get("url")
