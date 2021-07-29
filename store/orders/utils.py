from django.urls import reverse
from orders.models import Order

def get_or_create_order(request, cart):
    order = cart.order
    
    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)
    
    if order:
        request.session['order_id'] = order.order_id
    return order

def breadcrumb(products=True, addres=False, payment=False, confirmation=False):
    return [
        {'title':'Productos', 'active':products, 'url': reverse('orders:order')},
        {'title':'Dirección', 'active':addres, 'url': reverse('orders:order')},
        {'title':'Pago', 'active':payment, 'url': reverse('orders:order')},
        {'title':'Confirmación', 'active':confirmation, 'url': reverse('orders:order')},
    ]
