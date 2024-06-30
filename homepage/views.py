from django.shortcuts import render
from .models import OTP
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import random
from rest_framework import exceptions
from .models import Product
from user.models import User


class Alluser():
    def __init__(self,request):
        self.session = request.session
        #get the current session key if it exists
        list = self.session.get('session_key')
        #if the user is new, no session key! create one!
        if 'session_key' not in request.session:
            list = list.session['session_key'] = {}

        #make sure list is avaliable on all pages of site
        self.list = list
       
    def add(self, order):
        order_id = str(order.id)
        #logic
        if order_id in self.list:
            pass
        else:
            self.list[order_id] = {'price' : str(order.price)}
        self.session.modified = True 
    def __len__(self):
        return len(self.cart)

    def delete(self, product):
        product_id = str(product)
        # Delete from dicitionary/cart
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
  

