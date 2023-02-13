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
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
from rest_framework.response import Response

# Create your views here.



# instantiate payment gateway
# gateway = 


def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)

    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))

    return Response()
    