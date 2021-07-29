import uuid
from enum import Enum
from django.db import models
from django.contrib.auth.models import User
from carts.models import Cart
from django.db.models.signals import pre_save

#Creamos una clase Order con un atributo 'status' al cual le pasamos el parametro choices
#Que es una lista de tuplas que itera la clase OrderStatus que hereda de la clase Enum(sirve para crear constantes enumeradas)

class OrderStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

choices = [ (tag, tag.value) for tag in OrderStatus ]


class Order(models.Model):
    order_id = models.CharField(max_length=100, blank=False, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_total = models.DecimalField(default=5, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=choices,
                             default=OrderStatus.CREATED)


    def __str__(self):
        return self.order_id

    def update_total(self):
        self.total = self.get_total()
        self.save()

    def get_total(self):
        return self.cart.total + self.shipping_total

    
def set_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()    

pre_save.connect(set_order_id, sender=Order)
pre_save.connect(set_total, sender=Order)
