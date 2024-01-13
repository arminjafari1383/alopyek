from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    address_sender = models.TextField()
    address_Receiver = models.TextField()
    name_product = models.CharField(max_length=400)
    price = models.FloatField(help_text="Price in Rial")
    price_transfer = models.FloatField(help_text="Price in Rial")
    
    def __str__(self) -> str:
        return self.name_product

