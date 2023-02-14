from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'full_name', 'phone_number', 'password']


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['gender', 'date_of_birth', 'customer', 'photo', 'address']

