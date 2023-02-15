from django.contrib import admin

from .models import Order

# Register your models here.



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'order_tracking_number', 
        'order_taxes', 'order_state', 'address', 
        'estimated_delivery_time', 'order_code', 'cart',
    ]




