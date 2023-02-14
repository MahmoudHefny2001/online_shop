from rest_framework import serializers

from .models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    model = Coupon
    fields = '__all__'


