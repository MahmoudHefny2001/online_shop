from django.db import models
from customer.models import Customer
from product.models import Product

# Create your models here.


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    has_discount = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=3)
