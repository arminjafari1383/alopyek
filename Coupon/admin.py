from django.contrib.admin import ModelAdmin, register
from .models import Coupon


@register(Coupon)
class CouponAdmin(ModelAdmin):
    pass