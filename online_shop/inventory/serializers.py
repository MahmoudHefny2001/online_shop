from rest_framework import serializers
from .models import Inventory
from location.serializers import AddressSerializer

class InventorySerializer(serializers.ModelSerializer):
    location = AddressSerializer()
    class Meta:
        model = Inventory
        fields = ['name', 'location']