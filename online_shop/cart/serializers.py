from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework.serializers import ModelSerializer
from product.serializers import ProductsReadSerializer
from discount.serializers import DiscountReadSerializer
from .models import Cart
from merchant.serializers import MerchantSerializer

class CartSerializer(ModelSerializer):
    discount = DiscountReadSerializer()
    class Meta:
        model = Cart
        fields = ['product', 'discount', 'quantity']


class CartRead(ModelSerializer):
    product = ProductsReadSerializer()
    discount = DiscountReadSerializer()
    
    class Meta:
        model = Cart
        fields = ['product', 'discount', 'quantity', 'product', 'discount']