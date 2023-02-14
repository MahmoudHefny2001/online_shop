from django.contrib.auth.hashers import make_password
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from location.serializers import AddressSerializer

from .models import Customer, Profile


class ProfileSerializer(WritableNestedModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Profile
        fields = ['gender','date_of_birth','address', 'photo', 'customer']


 
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username','full_name','email','password', 'phone_number']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
     
    def create(self, validated_data):
        user = Customer.objects.create(
            phone_number = validated_data['phone_number'],
            email = validated_data['email'],
            user_name = validated_data['username'],
            full_name = validated_data['full_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username_or_email_or_phone = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=250)



class PasswordResetSerializer(serializers.Serializer):
    model = Customer
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)