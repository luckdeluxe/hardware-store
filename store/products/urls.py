from django.urls import path
from .views import *


#app_name = 'products'

urlpatterns = [
    path('search', ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', ProductDetailView.as_view(), name='product'),
]
