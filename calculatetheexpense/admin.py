from django.contrib.admin import ModelAdmin, register
from .models import Order

@register(Order)
class OrderAdmin(ModelAdmin):
    pass
    # autocomplete_fields = ['address_sender',' address_Receiver']
    # list_display = ['name', 'address_sender', ' address_Receiver']