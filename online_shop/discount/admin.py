from django.contrib import admin

from . import models


@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['code', 'available']
