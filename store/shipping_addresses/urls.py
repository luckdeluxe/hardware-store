from django.urls import path
from shipping_addresses.views import ShippingAddressDeleteView, ShippingAddressListView, ShippingAdressUpdateView, create

app_name = 'shipping_addresses'

urlpatterns = [
    path('', ShippingAddressListView.as_view(), name='shipping_addresses'),
    path('new', create, name='create'),
    path('edit/<int:pk>', ShippingAdressUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ShippingAddressDeleteView.as_view(), name='delete'),
]