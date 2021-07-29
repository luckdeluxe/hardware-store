from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cart', 'shipping_total', 'total', 'status', 'created_at')

admin.site.register(Order, OrderAdmin)
