from django.urls import path
from .views import *

app_name = 'carts'

urlpatterns = [
    path('', cart, name='cart'),
    path('add', add, name='add'),
    path('remove', remove, name='remove'),

]
