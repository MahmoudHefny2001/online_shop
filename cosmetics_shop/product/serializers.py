from rest_framework import serializers
from .models import Product, Category, Order, Brand, ImageModel, Address
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from drf_writable_nested.serializers import WritableNestedModelSerializer



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['line1','line2','city','governorate', 'zipCode']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'
