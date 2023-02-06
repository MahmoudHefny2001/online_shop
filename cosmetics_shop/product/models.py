from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
from merchant.models import Inventory 
from datetime import datetime    


# Create your models here.



class Address(models.Model):
    line1 = models.CharField(max_length=50, blank=True, null=True)
    line2 = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=False, blank=True, default='Assiut')
    governorate = models.CharField(max_length=30, blank=True, null=True, default='Assiut')
    zipCode = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.line1 + ' ' + self.line2


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    description = models.TextField(max_length=500, default="")

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    collection_images = models.ForeignKey('ImageModel', blank=True, on_delete=models.CASCADE)

    product_available = models.BooleanField(default=True, null=True, blank=True)
    discount_available = models.BooleanField(default=True, null=True, blank=True)

    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, default=1) 

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)


# class SupProduct(models.Model):
#     pass


class ImageModel(models.Model):
    images = models.ImageField(upload_to='products', blank=True) 


class Order(models.Model):
    ORDER_STATE = (
        ('Arrived','Arrived'),
        ('Not Arrived','Not Arrived'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    order_tracking_number = models.CharField(max_length=100, unique=True, null=False, db_index=True, default="50-50")
    order_taxes = models.FloatField(default=50)
    order_state = models.CharField(max_length=12, choices=ORDER_STATE, default='Not Arrived', null=False, blank=False)
    order_amount = models.PositiveIntegerField(default=1)
    address = models.ForeignKey('Address', on_delete=models.PROTECT, default="Assiut")

    estimated_delivery_time = models.DateField(default=datetime.now)



class Brand(models.Model):
    name = models.CharField(max_length=100)
