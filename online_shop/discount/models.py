from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Discount(TimeStampedModel):
    code = models.CharField(max_length=100, unique=True)
    available = models.BooleanField(default=False)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    