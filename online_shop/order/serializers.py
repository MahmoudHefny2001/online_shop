from rest_framework import serializers
from .models import Order
from cart.serializers import CartSerializer, CartRead
from product.serializers import ProductSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from location.serializers import AddressSerializer
from customer.serializers import CustomerSerializer
from product.serializers import ProductsReadSerializer

class OrderSerializer(WritableNestedModelSerializer):
    cart = CartRead()
    address = AddressSerializer()
    customer = CustomerSerializer()
    
    class Meta:
        model = Order
        fields = [
            'address', 'cart', 'customer', 
            'created', 'order_taxes', 'order_state',
            'estimated_delivery_time', 'total_price'
        ]
        read_only_field = ('price', 'order_taxes')
    

class OrderCreateSerializer(WritableNestedModelSerializer):
    cart = CartSerializer()
    class Meta:
        model = Order
        fields = ['address', 'cart']
        read_only_field = ('price')
        
