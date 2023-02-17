from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['line', 'city', 'governorate', 'zipCode']



class ShippingAddressSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize address of type shipping
    For shipping address, automatically set address type to shipping
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['address_type'] = 'S'

        return representation


class BillingAddressSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize address of type billing
    For billing address, automatically set address type to billing
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['address_type'] = 'B'

        return representation