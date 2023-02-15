from django.shortcuts import render
from rest_framework import viewsets
from .models import Merchant
from .serializers import MerchantSerializer

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
