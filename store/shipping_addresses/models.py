from django.db import models

from django.contrib.auth.models import User


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1= models.CharField(max_length=50)
    line2= models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    reference = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.postal_code

    @property
    def address(self):
        return '{} - {} - {}'.format(self.city, self.state, self.country)