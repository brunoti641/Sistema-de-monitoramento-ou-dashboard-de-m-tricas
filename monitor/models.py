from django.db import models
class Device(models.Model):
    device_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f'{self.device_id} ({self.name})'
class Event(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='events')
    timestamp = models.DateTimeField(db_index=True)
    metric = models.CharField(max_length=100, db_index=True)
    value = models.FloatField()
    raw_payload = models.JSONField(null=True, blank=True)
    class Meta:
        ordering = ['-timestamp']
