from rest_framework import serializers

from .models import Coupon, Discount


class CouponSerializer(serializers.ModelSerializer):
    model = Coupon
    fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    model = Discount
    fields = '__all__'