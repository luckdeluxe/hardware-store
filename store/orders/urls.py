from django.urls import path
from orders.views import OrderListView, address, cancel, check_address, confirm, order, payment, select_address, complete

app_name = 'orders'

urlpatterns = [
    path('', order, name='order'),
    path('address', address, name='address'),
    path('select/address', select_address, name='select_address'),
    path('check/address/<int:pk>', check_address, name='check_address'),
    path('confirm', confirm, name='confirm'),
    path('cancel', cancel, name='cancel'),
    path('complete', complete, name='complete'),
    path('completed', OrderListView.as_view(), name='completed'),
    path('payment', payment, name='payment'),
]