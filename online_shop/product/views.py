from django.shortcuts import render
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)

from .serializers import (BrandSerializer, CategorySerializer, ImageSerializer,
                          ProductSerializer, ProductsSerializer)

from.models import(Product, Category, ImageModel, Brand,)
from rest_framework import filters, viewsets
from rest_framework.response import Response

from . import models


class CategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

    
class ProductsView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)

class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)



class ImageAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer  
    
    


class BrandView(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

