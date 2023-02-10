from django.db import models
from customer.models import Customer
from location.models import Address
from cart.models import Cart
from datetime import datetime

# Create your models here.



class Order(models.Model):
    ORDER_STATE = (
        ('Arrived','Arrived'),
        ('Not Arrived','Not Arrived'),
    )
    
    created_at = models.DateTimeField(default=datetime.now)
    order_tracking_number = models.CharField(max_length=100, unique=True, null=False, db_index=True)
    order_taxes = models.FloatField(default=50)
    order_state = models.CharField(max_length=12, choices=ORDER_STATE, default='ARRIVED', null=False, blank=False)
    order_amount = models.PositiveIntegerField(default=1)
    estimated_delivery_time = models.DateField(default=datetime.now)

    address = models.ForeignKey('location.Address', on_delete=models.PROTECT)
    
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT)
    cart = models.OneToOneField(Cart, on_delete=models.PROTECT)