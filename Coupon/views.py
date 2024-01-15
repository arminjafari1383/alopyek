from django.http.response import HttpResponse, JsonResponse
from .models import Coupon
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import couponSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user.authentication import JWTAuthentication

class couponView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = couponSerializer

class couponView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = couponSerializer
