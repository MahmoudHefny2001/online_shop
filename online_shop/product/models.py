from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    description = models.TextField(max_length=500)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    available = models.BooleanField(default=True)

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)    
    category = models.ForeignKey('product.Category', related_name='products', on_delete=models.PROTECT)
    discount = models.ForeignKey('discount.Discount', on_delete=models.PROTECT, blank=True, null=True)
    merchant = models.ForeignKey('merchant.Merchant', on_delete=models.PROTECT) 
    

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)


class ImageModel(models.Model):
    image = models.ImageField(upload_to='products', blank=True)
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT, null=True)


class ProductReview(models.Model):
    customer = models.ManyToManyField('customer.Customer')
    comment = models.TextField(null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)


