from django.db import models
from django_extensions.db.models import TimeStampedModel
from payments import PurchasedItem
from payments.models import BasePayment
from django.utils.translation import gettext_lazy as _



class Payment(TimeStampedModel):
    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'

    STATUS_CHOICES = ((PENDING, _('pending')), (COMPLETED,
                      _('completed')), (FAILED, _('failed')))

    # Payment options
    PAYPAL = 'P'
    STRIPE = 'S'

    PAYMENT_CHOICES = ((PAYPAL, _('paypal')), (STRIPE, _('stripe')))

    code = models.CharField(max_length=200, unique=True, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    payment_option = models.CharField(max_length=1, choices=PAYMENT_CHOICES)
    
    order = models.OneToOneField('order.Order', related_name='payment', on_delete=models.PROTECT)
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.order.customer.full_name