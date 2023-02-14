from django.contrib import admin
from . import models

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['line', 'city', 'governorate', 'zipCode']
