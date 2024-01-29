from django.shortcuts import render
from .models import OTP
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import random
from rest_framework import exceptions

#this function for show main page
def mainpage(request):
    return render(request, 'homepage/index.html')
#this class for genrate otp code
class OTPgenrate(APIView):

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
