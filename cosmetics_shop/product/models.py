from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
from merchant.models import Inventory 
from datetime import datetime    
from location.models import Address

# Create your models here.


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
    category = models.ForeignKey('Category', related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
    product = models.ForeignKey('Product', on_delete=models.PROTECT, default='')


class Order(models.Model):
    ORDER_STATE = (
        ('Arrived','Arrived'),
        ('Not Arrived','Not Arrived'),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=datetime.now)
    order_tracking_number = models.CharField(max_length=100, unique=True, null=False, db_index=True)
    order_taxes = models.FloatField(default=50)
    order_state = models.CharField(max_length=12, choices=ORDER_STATE, default='ARRIVED', null=False, blank=False)
    order_amount = models.PositiveIntegerField(default=1)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    estimated_delivery_time = models.DateField(default=datetime.now)



class Brand(models.Model):
    name = models.CharField(max_length=100)
