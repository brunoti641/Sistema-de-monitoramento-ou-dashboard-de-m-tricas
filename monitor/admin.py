from django.contrib import admin
from .models import Device, Event
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id','name','location')
    search_fields = ('device_id','name')
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('device','metric','value','timestamp')
    list_filter = ('metric',)
    search_fields = ('device__device_id',)
