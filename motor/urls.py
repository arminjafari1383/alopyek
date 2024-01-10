from django.urls import path
from .views import (
    CreateMotorStation,
    MotorStationView
)
urlpatterns =[
    path('createmotorstation', CreateMotorStation.as_view(), name='createmotorstation'),
    path('viewmotorstation', MotorStationView.as_view(),name = 'viewmotorstation')
]