from django.db import models
from customer.models import Customer
from location.models import Address
from cart.models import Cart
from datetime import datetime
from django_extensions.db.models import TimeStampedModel
# Create your models here.



class Order(TimeStampedModel):
    ORDER_STATE = (
        ('Arrived','Arrived'),
        ('Not Arrived','Not Arrived'),
    )
    
    order_tracking_number = models.CharField(max_length=100, unique=True, null=False, db_index=True)
    order_taxes = models.FloatField(default=50)
    order_state = models.CharField(max_length=12, choices=ORDER_STATE, default='Not Arrived', null=False, blank=False)
    
    order_amount = models.PositiveIntegerField(default=1)
    
    estimated_delivery_time = models.DateField(default=datetime.now)

    address = models.ForeignKey('location.Address', on_delete=models.PROTECT)
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)
    cart = models.ForeignKey('cart.Cart', on_delete=models.PROTECT)
    discount = models.ForeignKey('discount.Discount', on_delete=models.PROTECT, default=0)

    total_price = models.DecimalField(max_digits=10, decimal_places=3)

    def Total_Price(self):
        total = self.order_amount * self.cart.price_per_item
        return total


class OrderItem(models.Model):
    code = models.CharField(max_length=200, unique=True)
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def Total_Price(self):
        total = self.order_amount * self.product.price
        return total