from django.urls import path
from .views import (
    PaymentRetrieve,PaymentRetrieve2
)

urlpatterns = [
    path('PaymentRetrieve', PaymentRetrieve.as_view(), name='PaymentRetrieve'),
    path('PaymentRetrieve2/<int:pk>', PaymentRetrieve2.as_view(), name='PaymentRetrieve2')
]