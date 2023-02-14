from datetime import datetime
from django.db import models
from django_extensions.db.models import TimeStampedModel

class Order(TimeStampedModel):
    ORDER_STATE = (
        ('Arrived','Arrived'),
        ('Not Arrived','Not Arrived'),
    )
    
    order_tracking_number = models.CharField(max_length=100, unique=True, null=False, db_index=True)
    order_taxes = models.FloatField(default=50)
    order_state = models.CharField(max_length=12, choices=ORDER_STATE, default='Not Arrived')
    order_code = models.CharField(max_length=200, unique=True)
    order_amount = models.PositiveIntegerField(default=1)
    estimated_delivery_time = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    address = models.ForeignKey('location.Address', on_delete=models.PROTECT)
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)
    cart = models.ForeignKey('cart.Cart', on_delete=models.PROTECT)
    discount = models.ForeignKey('discount.Discount', on_delete=models.PROTECT)


    def Total_Price(self):
        total_price = self.order_amount * self.cart.product.price
        return total

