from .models import MotorStation,Motor,Travel
from rest_framework.serializers import ModelSerializer,CharField
"""
create three class with rest and serilazed

"""

class MotorstationSerializer(ModelSerializer):
    class Meta:
        model = MotorStation
        fields = ('city',)



class MotorSerializer(ModelSerializer):
    latitude = MotorstationSerializer()
    longitude = MotorstationSerializer()
    class Meta:
        model = Motor
        fields = '__all__'


class TravelSerializer(ModelSerializer):
    reservation_code = CharField(required=False)
    user = CharField(required=False)
    class Meta:
        model = Travel
        fields = '__all__'


