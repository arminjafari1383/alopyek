from django.urls import path
from .views import OrderView,OrderView2
urlpatterns = [
    path('OrderView', OrderView.as_view(), name='OrderView'),
    path('OrderView2/<int:pk>', OrderView2.as_view(), name='OrderView2')

]