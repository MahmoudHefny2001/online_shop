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
from.models import(
    Product,
    Category, 
    ImageModel,
    Order, 
    Brand,
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import generics, mixins, viewsets, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from . import models
from rest_framework.response import Response

# Create your views here.

class CategoryView(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (AllowAny)
    permission_classes = (AllowAny)


class ProductView(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (AllowAny)
    permission_classes = (AllowAny)


class ImageView(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = (AllowAny)
    permission_classes = (AllowAny)


class BrandView(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes = (AllowAny)
    permission_classes = (AllowAny)




