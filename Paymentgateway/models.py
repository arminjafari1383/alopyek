from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    card_number = models.CharField(max_length=11)
    cvv2_number = models.CharField(max_length=4)
    time = models.DateTimeField()
    code = models.CharField(max_length=4)