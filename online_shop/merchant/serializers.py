from rest_framework import serializers

from .models import Merchant
from inventory.serializers import InventorySerializer

class MerchantSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer()
    class Meta:
        model = Merchant
        fields = ['name', 'address', 'phone_number', 'postal_code', 'fax', 'email', 'inventory']
