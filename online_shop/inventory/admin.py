from django.contrib import admin
from . import models

@admin.register(models.Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
