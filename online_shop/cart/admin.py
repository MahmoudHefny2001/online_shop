from django.contrib import admin
from . import models


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'discount', 'quantity']