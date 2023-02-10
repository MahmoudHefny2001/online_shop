from django.db import models

from customer.models import Customer

from merchant.models import Inventory 
from datetime import datetime    
from location.models import Address
from django.core.validators import MaxValueValidator, MinValueValidator


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
    category = models.ForeignKey('product.Category', related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True, blank=True)
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


class ImageModel(models.Model):
    images = models.ImageField(upload_to='products', blank=True) 
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT, default='')


class Brand(models.Model):
    name = models.CharField(max_length=100)



class ProductReview(models.Model):
    customer = models.ManyToManyField(Customer)
    comment = models.TextField(max_length=300, null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True, blank=True)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, default='1')


# class SupProduct(models.Model):
#     pass