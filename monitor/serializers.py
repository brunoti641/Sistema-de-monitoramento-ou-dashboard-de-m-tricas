from rest_framework import serializers
from .models import Device, Event
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id','device_id','name','location')
class EventSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    class Meta:
        model = Event
        fields = ('id','device','timestamp','metric','value')
