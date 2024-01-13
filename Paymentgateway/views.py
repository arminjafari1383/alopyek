from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import Payment
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import PaymentSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user.authentication import JWTAuthentication
from time import sleep



class PaymentRetrieve(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieve2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer