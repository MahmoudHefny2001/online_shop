from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.


class Cart(TimeStampedModel):
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT)
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)

    quantity = models.IntegerField(default=1)
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
    has_discount = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    