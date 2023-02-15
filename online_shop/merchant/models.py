from django.db import models
from location.models import Address


class Merchant(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.ForeignKey('location.Address', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True, db_index=True)
    postal_code = models.CharField(max_length=30)
    fax = models.CharField(max_length=20)
    email = models.CharField(max_length=200, unique=True, db_index=True)
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.SET_NULL, null=True)

