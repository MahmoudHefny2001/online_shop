from rest_framework.serializers import ModelSerializer

from .models import Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'discount', 'quantity', 'price_per_item']