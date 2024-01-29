from django.db import models


#this class for otp input(get phone number)
class OTP(models.Model):
    phone_number = models.CharField(max_length=20)
    