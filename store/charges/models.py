from django.db import models
from django.db.models.fields import CharField
from stripe.api_resources import payment_method
from users.models import User
from orders.models import Order
from stripeAPI.charges import create_charge as create_charge_stripe

class ChargesManager(models.Manager):

    def create_charge(self, order):
        charge = create_charge_stripe(order)

        return self.create(
            user = order.user,
            order = order,
            charge_id = charge.id,
            amount = charge.amount,
            payment_method = charge.payment_method,
            status = charge.status
        )


class Charges(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    charge_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ChargesManager()

    def __str__(self):
        return self.charge_id

    
