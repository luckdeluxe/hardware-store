from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total', 'cart_id', 'created_at')

admin.site.register(Cart, CartAdmin)
