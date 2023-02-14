from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug' ,'active' ,'description']
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','name', 'slug','image', 'description', 'price', 'available']


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['image']

