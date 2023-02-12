from django.shortcuts import render
from django.conf import settings
from order.models import Order
from .tasks import payment_completed

from rest_framework.authentication import(SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework import generics, mixins, viewsets, views
from . import serializers
from location.serializers import AddressSerializer
from . import models
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.db.models.signals import pre_save, post_save
from rest_framework import status

# Create your views here.



# instantiate payment gateway
# gateway = 


class PaymentProcess(viewsets.ModelViewSet):
    # order_id =
    # order = 
    total_cost = order.total_price
    pass
    