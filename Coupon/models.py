from django.db import models
from django.contrib.auth.models import User

class Coupon(models.Model):
    name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=11)
    capacity = models.IntegerField()
    def __str__(self) -> str:
        return self.name
