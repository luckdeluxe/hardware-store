from django.db import models
from products.models import Product

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

