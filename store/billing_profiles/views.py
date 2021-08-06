from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from billing_profiles.models import BillingProfile
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class BillingProfileListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'billing_profiles/billing_profiles.html'

    def get_queryset(self):
        return self.request.user.billing_profiles

@login_required(login_url='login')
def create(request):

    if request.method == 'POST':
        if request.POST.get('stripeToken'):

            if not request.user.has_customer():
                request.user.create_customer_id()

            stripe_token = request.POST['stripeToken']    
            billing_profile = BillingProfile.objects.create_by_stripe_token(request.user, stripe_token)
            
            if billing_profile:
                messages.success(request, 'Tarjeta creada con éxito')

    return render(request, 'billing_profiles/create.html', {

    })
