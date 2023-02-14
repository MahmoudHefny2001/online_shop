from django.contrib import admin
from . import models


@admin.register(models.Merchant)
class MerchantyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number', 'postal_code', 'fax', 'email']