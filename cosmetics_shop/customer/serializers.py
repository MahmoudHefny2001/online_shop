from rest_framework import serializers
from django.core.validators import RegexValidator
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile, Address, Customer
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['line1', 'line2', 'city', 'governorate', 'zipCode']
        read_only_fields = ("id", )


class AddressSerializer(serializers.Serializer):
    line1 = serializers.CharField(required=False, allow_null=True)
    line2 = serializers.CharField(required=False, allow_null=True)
    city = serializers.CharField(required=False, allow_null=True)
    governorate = serializers.CharField(required=False, allow_null=True)
    zipCode = serializers.CharField(required=False, allow_null=True)


class ProfileSerializer(serializers.Serializer):
    
    address = AddressSerializer(required=False, allow_null=True)

    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
    )

    gender = serializers.ChoiceField(choices=GENDER_CHOICES, default='Male', allow_null=True)
    date_of_birth = serializers.DateField(allow_null=True)

    photo = serializers.FileField(
        allow_null=True, 
        required=False, use_url=True,
        max_length=None, source='profile.photo',
        allow_empty_file=True,        
    )

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