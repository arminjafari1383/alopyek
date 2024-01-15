from django.urls import path
from .views import(
    couponView,couponView2
)

urlpatterns = [
    path('couponView', couponView.as_view(), name='couponView'),
    path('couponView2/<int:pk>', couponView2.as_view(), name='couponView2')
]