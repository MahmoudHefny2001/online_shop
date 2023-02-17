from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.functional import cached_property


class Cart(TimeStampedModel):
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT)
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)
    discount = models.ForeignKey('discount.Discount', on_delete=models.PROTECT, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.customer.full_name
    
    @cached_property
    def cost(self):
        return round(self.quantity * self.product.price, 2)
         


    

    