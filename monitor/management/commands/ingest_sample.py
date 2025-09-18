from django.core.management.base import BaseCommand
import random, time
from monitor.models import Device
class Command(BaseCommand):
    help = 'Generate sample sensor events (async via Celery)'
    def handle(self, *args, **options):
        device, _ = Device.objects.get_or_create(device_id='device_1', defaults={'name':'Sensor 1'})
        from monitor.tasks import write_event
        for i in range(50):
            metric = 'temperature'
            value = random.uniform(20.0, 30.0)
            write_event.delay(device.id, metric, value, None)
            time.sleep(0.05)
        self.stdout.write(self.style.SUCCESS('Sample ingestion queued.'))
