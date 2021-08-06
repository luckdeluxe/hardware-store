import uuid, decimal
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.db import models
from users.models import User
from django.db.models.fields import DecimalField
from products.models import Product
from orders.common import OrderStatus
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProducts')
    subtotal = DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)

    FEE = 0.05 # Comision del 5%

    def __str__(self):
        """Retornamos el usuario al cual pertenece el carro"""
        return str(self.user)

    def update_totals(self):
        self.update_subtotal()
        self.update_total()

        if self.order:
            self.order.update_total()

    def update_subtotal(self): # Usamos list comprehension para sumar la lista SELF.products.all() = todos los productos del carrito
        self.subtotal = sum([
            cp.quantity * cp.product.price for cp in self.products_related()
        ])
        self.save()

    def update_total(self): # Hacemos la ecuación para calcular el valor total del carrito. (Subtotal + FEE)
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()

    def products_related(self):
        return self.cartproducts_set.select_related('product')

    def has_products(self):
        return self.products.exists()

    @property
    def order(self):
        return self.order_set.filter(status=OrderStatus.CREATED).first()

class CartProductsManager(models.Manager):
    def create_or_update_quantity(self, cart, product, quantity=1):
        object, created = self.get_or_create(cart=cart, product=product)

        if not created:
            quantity = object.quantity + quantity
        object.update_quantity(quantity)
        return object


class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartProductsManager()
    
    def update_quantity(self, quantity=1):
        self.quantity = quantity
        self.save()
    

def set_cart_id(sender, instance, *args, **kwargs):
    """Creamos un nuevo ID para el carro de forma aleatoria usando uuid y signals con pre_save"""
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())


def update_totals(sender, instance, action, *args, **kwargs): # Condicionamos las acciones, ejecutando la funcion update_totals()
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()


def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.cart.update_totals()


#Ejecución de callbacks
pre_save.connect(set_cart_id, sender=Cart)
post_save.connect(post_save_update_totals, sender=CartProducts)
m2m_changed.connect(update_totals, sender=Cart.products.through)