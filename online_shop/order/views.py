from django.shortcuts import render
from rest_framework import generics, views, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from .models import Order
from .serializers import  OrderSerializer, OrderCreateSerializer


class OrderAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.user.id)

    


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.user.id)





