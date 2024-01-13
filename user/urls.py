from django.urls import path
from .views import OTPView, LoginView,Travelregistration

urlpatterns = [
    path('generate-otp', OTPView.as_view(), name='generate-otp'),
    path('login', LoginView.as_view(), name='login'),
    path('getlocation',Travelregistration.as_view(),name='getlocation')
]