from django.urls import path
from .views import (
    MotorStation
)
urlpatterns =[
    path('motor', MotorStation.as_view(), name='motor'),
    path('list', list, name='list')
]