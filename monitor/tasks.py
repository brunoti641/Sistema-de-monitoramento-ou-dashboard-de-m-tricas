from celery import shared_task
from .models import Device, Event
from django.conf import settings
from influxdb_client import InfluxDBClient, Point, WritePrecision
import datetime
@shared_task
def write_event(device_id, metric, value, timestamp=None):
    try:
        device = Device.objects.get(pk=device_id)
    except Device.DoesNotExist:
        return
    ts = None
    if timestamp:
        try:
            ts = datetime.datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        except Exception:
            ts = datetime.datetime.utcnow()
    else:
        ts = datetime.datetime.utcnow()
    # save in local DB (meta)
    Event.objects.create(device=device, metric=metric, value=value, timestamp=ts, raw_payload={'value':value})
    # write to Influx if configured
    influx_cfg = getattr(settings, 'INFLUX', {})
    if influx_cfg and influx_cfg.get('URL'):
        try:
            with InfluxDBClient(url=influx_cfg['URL'], token=influx_cfg['TOKEN'], org=influx_cfg['ORG']) as client:
                write_api = client.write_api(write_options=WritePrecision.NS)
                p = Point(metric).tag('device_id', device.device_id).field('value', float(value)).time(ts, WritePrecision.NS)
                write_api.write(bucket=influx_cfg['BUCKET'], record=p)
        except Exception as e:
            # in production you'd log this
            pass
