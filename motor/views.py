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

class MotorStationView(generics.ListCreateAPIView):
    queryset = MotorStation.objects.all()
    serializer_class = MotorstationSerializer

class MotorStationView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = MotorStation.objects.all()
    serializer_class = MotorstationSerializer

class MotorView(generics.ListCreateAPIView):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer

class MotorView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer

class TravelView(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class =  TravelSerializer

class TravelView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class =  TravelSerializer