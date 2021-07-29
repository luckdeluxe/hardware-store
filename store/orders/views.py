from django.shortcuts import render
from orders.utils import get_or_create_order, breadcrumb
from carts.utils import get_or_create_cart
from orders.models import Order
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(request, cart)
    return render(request, 'orders/order.html', {
        'cart': cart,
        'order': order,
        'breadcrumb': breadcrumb()
    })

