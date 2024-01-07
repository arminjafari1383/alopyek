from django.contrib.admin import ModelAdmin, register
from .models import MotorStation,Motor , Travel
"""
create decorator for register and each class have adiffernet parametr

"""

@register(Motor)
class MotorAdmin(ModelAdmin):
    autocomplete_fields = ['latitude','longitude']
    list_display = ['name', 'latitude', 'longitude']


@register(MotorStation)
class MotorStationAdmin(ModelAdmin):
    list_display = ["name","no","city","phone_number"]
    search_fields = ["name",]
    list_filter = ['name','city']


@register(Travel)
class TravelAdmin(ModelAdmin):
    list_display = ['name', 'lastname', 'reservation_code']