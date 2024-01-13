from django.contrib.admin import ModelAdmin, register
from .models import Payment


@register(Payment)
class PaymentAdmin(ModelAdmin):
    pass

