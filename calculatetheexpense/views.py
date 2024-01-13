from django.http.response import HttpResponse, JsonResponse
from .models import Order
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import orderserializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user.authentication import JWTAuthentication
from time import sleep
# Create your views here.

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = orderserializers
class OrderView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = orderserializers
        