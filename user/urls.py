from django.urls import path
from .views import OTPView, LoginView,Travelregistration

urlpatterns = [
    path('generate-otp', OTPView.as_view(), name='generate-otp'),
    path('login', LoginView.as_view(), name='login'),
    path('getlocation',Travelregistration.as_view(),name='getlocation'),
    path('user', CreateUser.as_view(),name='user'),
    path('user',Createneworder.as_view(),name = 'createnewuser')
]