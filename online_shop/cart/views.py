from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from .models import Cart
from .serializers import CartSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


# Create your views here.


class CartAPIView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication) 
    permission_classes = (IsAuthenticated)