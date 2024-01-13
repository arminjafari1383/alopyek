from .models import Order
from rest_framework.serializers import ModelSerializer,CharField
"""
create three class with rest and serilazed

"""

class orderserializers(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'