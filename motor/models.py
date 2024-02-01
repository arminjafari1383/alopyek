from django.db import models
from django.contrib.auth.models import User
"""
class MotorStation for place all of motor park this station
class Motor for motor and use for new user for motor
class Travel for user can reserve travel
def str for show in table django

"""

class MotorStation(models.Model):
    name = models.CharField(max_length=400)
    no = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=11)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self) -> str:
        return self.name

class Motor(models.Model):
    latitude = models.ForeignKey(MotorStation, on_delete=models.CASCADE)
    longitude = models.ForeignKey(MotorStation, on_delete=models.CASCADE, related_name='destination_airport')
    name = models.CharField(max_length=255)
    no = models.CharField(unique=True,max_length=10, verbose_name="Code")
    price = models.FloatField(help_text="Price in Rial")
    def __str__(self) -> str:
        return "{} - {}".format(self.name,self.no)

class Travel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    Motor = models.ForeignKey(MotorStation, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    nationalid = models.CharField(max_length=10)
    reservation_code = models.CharField(max_length=8, unique=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.name, self.lastname)

#this class measuare cost travel travel
class Measuretravel(models.Model):
    distance = models.CharField(max_length=10)
    destination = models.CharField(max_length=20)

    def __str__(self) -> str:
        return '{} {}'.format(self.name)
