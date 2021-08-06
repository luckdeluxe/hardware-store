from django.urls import path
from billing_profiles.views import BillingProfileListView, create

app_name = 'billing_profiles'

urlpatterns = [
    path('', BillingProfileListView.as_view(), name='billing_profiles'),
    path('new', create, name='create'),
]