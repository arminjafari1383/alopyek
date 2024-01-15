from django.urls import path
from .views import (
    CreateMotorStation,
    MotorStationView,
)
urlpatterns =[
    path('createmotorstation', MotorStationView.as_view(), name='createmotorstation'),
    path('viewmotorstation/<int:pk>', MotorStationView2.as_view(),name = 'viewmotorstation'),
    path('createmotor',MotorView.as_view(),name = 'createmotor'),
    path('viewmotor/<int:pk>',MotorView2.as_view(),name = 'viewmotorstation'),
    path('createtravel',TravelView.as_view(),name = 'createtravel'),
    path('viewtravel/<int:pk>',TravelView2.as_view(),name = ''),
]