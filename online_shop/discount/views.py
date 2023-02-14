from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DiscountSerializer
from .models import Discount

class DiscountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    