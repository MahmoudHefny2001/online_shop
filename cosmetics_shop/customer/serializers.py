from rest_framework import serializers
from django.core.validators import RegexValidator
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile, Address, Customer
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from drf_writable_nested.serializers import WritableNestedModelSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['line1','line2','city','governorate', 'zipCode']
    
    

class ProfileSerializer(WritableNestedModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Profile
        fields = ['gender','date_of_birth','address', 'customer']


 
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