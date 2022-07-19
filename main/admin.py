from django.contrib import admin
from device.models import devices
# Register your models here.

# @admin.register(devices)
# class devicesAdmin(admin.ModelAdmin):
#     list_display: ('device_id',  'vehicle_no', 'route_name',  'temperature', 'carbon_mono',  'humidity', 'light', 'noise', 'langitude', 'latitude')