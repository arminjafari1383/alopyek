from .models import Payment
from rest_framework.serializers import ModelSerializer, CharField


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'