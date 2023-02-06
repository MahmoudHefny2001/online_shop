from django.db import models


# Create your models here.


class Address(models.Model):
    line1 = models.CharField(max_length=50, blank=True, null=True)
    line2 = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=False, blank=True, default='Assiut')
    governorate = models.CharField(max_length=30, blank=True, null=True, default='Assiut')
    zipCode = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.line1 + ' ' + self.line2



class Inventory(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True, db_index=True)
    postal_code = models.CharField(max_length=30)
    fax = models.CharField(max_length=20)
    email = models.CharField(max_length=200, unique=True, db_index=True)
