from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import(
    AddressSerializer,
    CategorySerializer,
    ProductSerializer,
    OrderSerializer,
    BrandSerializer,
    ImageSerializer,
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import generics, mixins, viewsets, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from . import models
from rest_framework.response import Response

# Create your views here.



