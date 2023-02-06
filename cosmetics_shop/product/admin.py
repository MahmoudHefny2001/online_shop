from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'active', 'description']
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'category','name',
        'slug','image', 
        'description', 'price', 
        'available','created', 'updated',
        'collection_images', 'product_available', 
        'discount_available', 'inventory'
    ]


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['images']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'customer', 'product',
        'created_at', 'order_tracking_number', 
        'order_taxes', 'order_state', 
        'order_amount', 'address', 
        'estimated_delivery_time'
    ]