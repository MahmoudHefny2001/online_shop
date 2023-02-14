from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import(
    CategorySerializer,
    ProductSerializer,
    BrandSerializer,
    ImageSerializer,
)
from.models import(
    Product,
    Category, 
    ImageModel,
    Brand,
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import generics, mixins, viewsets, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from . import models
from rest_framework.response import Response
from location.serializers import AddressSerializer

from rest_framework import filters

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.id)
    


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)


    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.id)



class ImageAPIView(viewsets.ModelViewSet):
    queryset = ImageModel.objects.filter()
    serializer_class = ImageSerializer

    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.id)

    
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset())
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.id)



