from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import Cart
from .serializers import CartSerializer

# Create your views here.


class CartAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication) 
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self, *args, **kwargs):
        # 
        # qs = super().get_queryset(*args, **kwargs)
        # return qs.filter(id = self.request.user.cart.customer.id)