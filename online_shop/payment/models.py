from django.db import models
from django_extensions.db.models import TimeStampedModel
from payments import PurchasedItem
from payments.models import BasePayment

# Create your models here.

class Payment(BasePayment, TimeStampedModel):
    code = models.CharField(max_length=200, unique=True, null=False)
    payment_method = models.CharField(max_length=200)
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    
