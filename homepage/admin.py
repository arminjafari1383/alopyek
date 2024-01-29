#import from django register and ModelAdmin
from django.contrib.admin import register,ModelAdmin
#import from model function OTP
from .models import OTP

#this decorator for adminotp
@register(OTP)
class OtpAdmin(ModelAdmin):
    pass