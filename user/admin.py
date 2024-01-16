from django.contrib.admin import ModelAdmin, register
from .models import User,OTP,COST


@register(User)
class userAdmin(ModelAdmin):
    pass
@register(OTP)
class otpAdmin(ModelAdmin):
    pass
@register(COST)
class COSTAdmin(ModelAdmin):
    pass

