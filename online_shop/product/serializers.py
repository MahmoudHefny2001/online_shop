from rest_framework import serializers
from .models import Product, Category, Brand, ImageModel
from location.models import Address
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'
