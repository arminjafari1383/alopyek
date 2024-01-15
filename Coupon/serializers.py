from .models import Coupon
from rest_framework.serializers import ModelSerializer, CharField


class couponSerializer(ModelSerializer):
    class Meta:
        model = Coupon