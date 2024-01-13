from django.http.response import HttpResponse, JsonResponse
from .models import MotorStation, Motor, Travel
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import MotorstationSerializer,MotorSerializer,TravelSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user.authentication import JWTAuthentication
from time import sleep

class CreateMotorStation(generics.CreateAPIView):
    queryset = MotorStation.objects.all()
    serializer_class =  MotorstationSerializer

class MotorStationView(generics.ListCreateAPIView):
    queryset = MotorStation.objects.all()
    serializer_class = MotorstationSerializer
class TravelCreate(generics.CreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    authentication_classes = [JWTAuthentication,]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = self.perform_create(serializer, request)
        headers = self.get_success_headers(serializer.data)
        return Response("Ticket Reserved with {} reservation code!".format(code), status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer, request):
        code = generate_reservation_code()
        serializer.save(
            reservation_code = code,
            user = request.user
        )
        return code
class TravelList(generics.ListAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    authentication_classes = [JWTAuthentication,]

    def list(self, request, *args, **kwargs):
        self.queryset = Travel.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)

# creat html for motor
# def html(request):
#     if request.method == 'POST':
#         latitude = request.POST['latitude']
#         longitude = request.POST['longitude']
#         # motor = Motor.objects.filter(origin__city=origin, destination__city=dest)
#         m_list ={
#             'motor' : motor
#         }
#         return render(request, 'motor/list.html', context=m_list)
#     return render(request, 'motor/list.html')
