from django.shortcuts import render
from rest_framework import views, viewsets, generics
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.Objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.user.customer.id)



class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.Objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.user.customer.id)



