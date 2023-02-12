from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class Discount(TimeStampedModel):
    available = models.BooleanField(default=False)
    discount_percentage = models.IntegerField()
    

class coupon(TimeStampedModel):
    discount = models.ForeignKey('Discount', on_delete=models.PROTECT)

