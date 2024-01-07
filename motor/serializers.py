from .models import MotorStation,Motor,Travel
from rest_framework.serializers import ModelSerializer,CharField
"""
create three class with rest and serilazed

"""

class MoterstationSerializer(ModelSerializer):
    class Meta:
        model = Moterstation
        fields = ('city',)



class MotorSerializer(ModelSerializer):
    latitude = MoterstationSerializer()
    longitude = MoterstationSerializer()
    class Meta:
        model = Motor
        fields = '__all__'


class TravelSerializer(ModelSerializer):
    reservation_code = CharField(required=False)
    user = CharField(required=False)
    class Meta:
        model = Ticket
        fields = '__all__'


