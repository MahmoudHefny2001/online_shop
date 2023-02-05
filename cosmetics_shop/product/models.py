from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Brand(models.Model):
    name = models.CharField(max_length=100)
