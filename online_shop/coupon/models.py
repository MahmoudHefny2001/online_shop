from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class Discount(TimeStampedModel):
    available = models.BooleanField(default=False)
    discount_amount = models.IntegerField()
    code = models.CharField(max_length=100, unique=True)


class Coupon(TimeStampedModel):
    discount = models.ForeignKey('Discount', on_delete=models.PROTECT)

