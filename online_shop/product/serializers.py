from rest_framework import serializers
from .models import Brand, Category, ImageModel, Product
from discount.serializers import DiscountSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'active', 'description']



class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['product', 'image']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand 
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    discount = DiscountSerializer()


    class Meta:
        model = Product
        fields = [
            'name', 'image' , 'description', 'price',
            'available', 'merchant', 'brand',
            'category', 'discount'
        ]
        


