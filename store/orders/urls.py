from django.urls import path
from orders.views import address, cancel, check_address, confirm, order, select_address

app_name = 'orders'

urlpatterns = [
    path('', order, name='order'),
    path('address', address, name='address'),
    path('select/address', select_address, name='select_address'),
    path('check/address/<int:pk>', check_address, name='check_address'),
    path('confirm', confirm, name='confirm'),
    path('cancel', cancel, name='cancel'),
]