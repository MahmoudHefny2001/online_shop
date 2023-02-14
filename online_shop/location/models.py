from django.db import models

# Create your models here.

class Address(models.Model):
    line = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=30, null=False, blank=True)
    governorate = models.CharField(max_length=30, blank=True, null=True)
    zipCode = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.line