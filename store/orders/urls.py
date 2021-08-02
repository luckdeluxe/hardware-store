from django.urls import path
from orders.views import address, check_address, order, select_address

app_name = 'orders'

urlpatterns = [
    path('', order, name='order'),
    path('address', address, name='address'),
    path('select/address', select_address, name='select_address'),
    path('check/address/<int:pk>', check_address, name='check_address'),
]