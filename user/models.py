from django.db import models
from django.contrib.auth.models import User


class OTP(models.Model):
    phone_number = models.CharField(max_length=20)
    otp = models.CharField(max_length=5)


class COST(models.Model):
    latitude = models.CharField(max_length=20)
    cost = models.CharField(max_length=5)

#register new user
class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()

