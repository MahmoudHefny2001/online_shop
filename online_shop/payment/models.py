from django.db import models
from django_extensions.db.models import TimeStampedModel
from decimal import Decimal
from payments import PurchasedItem
from payments.models import BasePayment

# Create your models here.

class Payment(BasePayment, TimeStampedModel):

    def get_failure_url(self):
        # Return a URL where users are redirected after
        # they fail to complete a payment:
        return f"http://example.com/payments/{self.pk}/failure"

    def get_success_url(self):
        # Return a URL where users are redirected after
        # they successfully complete a payment:
        return f"http://example.com/payments/{self.pk}/success"

    def get_purchased_items(self):
        yield PurchasedItem(
            name='',
            sku='',
            # quantity=,
            price=Decimal(),
            currency='EGP',
        )
