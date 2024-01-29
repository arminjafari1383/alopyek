from django.urls import path
from .views import OTPgenrate,mainpage


urlpatterns = [
    path('', mainpage , name='mainpage'),
    path('OTPgenrate',OTPgenrate.as_view(), name='otpgenrate')
    
]