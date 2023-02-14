from django.shortcuts import render
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)

from .serializers import (BrandSerializer, CategorySerializer, ImageSerializer,
                          ProductSerializer)

from.models import(Product, Category, ImageModel, Brand,)
from rest_framework import filters, viewsets
from rest_framework.response import Response

from . import models


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
