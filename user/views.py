from django.http.response import HttpResponse, JsonResponse
from .models import OTP,COST,User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import status
from user.authentication import JWTAuthentication
import json
import random
from rest_framework import exceptions
from .authentication import create_access_token, create_refresh_token
from django.contrib.auth.models import User


class OTPView(APIView):

    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone_number = body['phone_number']
        otp = random.randint(10000,99999)
        OTP.objects.create(
            phone_number = phone_number,
            otp = otp
        )
        return Response(otp)


class LoginView(APIView):

    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone = body['phone_number']
        otp = body['otp']
        try:
            saved_otp = OTP.objects.get(phone_number=phone)
            if saved_otp.otp == otp:
                # saved_otp.delete()
                try:
                    current_user = User.objects.get(username=phone)
                except:
                    current_user = User.objects.create(
                        username = phone,
                    )
                access_token = create_access_token(current_user.id)
                refresh_token = create_refresh_token(current_user.id)
                res = Response(access_token)
                res.set_cookie('refresh_token', refresh_token, httponly=True)
                return res
            else:
                return Response("Otp is Wrong!", status=403)
        except:
            return Response("Something is Wrong!", status=500)


class Travelregistration(APIView):
       def post(self, request):
        body = request.body
        body = json.loads(body)
        latitude = body['latitude']
        cost = random.randint(10000,99999)
        COST.objects.create(
            latitude = latitude,
            cost = cost
        )
        return Response(cost)

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Createneworder(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer        

