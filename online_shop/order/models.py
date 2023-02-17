from datetime import datetime
from django.db import models
from django_extensions.db.models import TimeStampedModel
from cart.models import Cart
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property


class Order(TimeStampedModel):
    ORDER_STATE = (
        ('Arrived','Arrived'),
        ('Not Arrived','Not Arrived'),
    )
    
    order_tracking_number = models.CharField(max_length=100, unique=True, null=False, db_index=True)
    order_taxes = models.FloatField(default=50)
    order_state = models.CharField(max_length=12, choices=ORDER_STATE)
    order_code = models.CharField(max_length=200, unique=True)
    estimated_delivery_time = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=3)
    
    address = models.ForeignKey('location.Address', on_delete=models.PROTECT)
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)
    # cart = models.ForeignKey('cart.Cart', on_delete=models.PROTECT)
    shipping_address = models.ForeignKey('location.Address', related_name='shipping_orders', on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        ordering = ('-created', )

    
    def __str__(self):
        return self.customer.full_name

    
    @cached_property
    def total_cost(self):
        return round(sum([order_item.cost for order_item in self.order_items.all()]), 2)



class OrderItem(TimeStampedModel):
    order = models.ForeignKey('order.Order', related_name="order_items", on_delete=models.PROTECT)
    product = models.ForeignKey('product.Product', related_name="product_orders", on_delete=models.PROTECT)
    
    quantity = models.IntegerField()


    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.order.customer.full_name

    @cached_property
    def cost(self):
        """
        Total cost of the ordered item
        """
        return round(self.quantity * self.product.price, 2)