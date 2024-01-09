from django.http.response import HttpResponse, JsonResponse
from .models import MotorStation, Motor, Travel
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import MotorstationSerializer,MotorSerializer,TravelSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# from user.authentication import JWTAuthentication
from time import sleep


class MotorStation(generics.ListAPIView):
    queryset = MotorStation.objects.all()
    serializer_class = MotorstationSerializer

