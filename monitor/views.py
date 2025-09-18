from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Device, Event
from .serializers import EventSerializer
from .tasks import write_event
class IngestView(APIView):
    def post(self, request):
        data = request.data
        device_id = data.get('device_id')
        metric = data.get('metric')
        value = data.get('value')
        timestamp = data.get('timestamp', None)
        if device_id is None or metric is None or value is None:
            return Response({'error':'device_id, metric and value are required'}, status=400)
        device, _ = Device.objects.get_or_create(device_id=device_id)
        write_event.delay(device.id, metric, float(value), timestamp)
        return Response({'status':'queued'})
class RecentMetricsView(generics.ListAPIView):
    serializer_class = EventSerializer
    def get_queryset(self):
        metric = self.request.query_params.get('metric', None)
        limit = int(self.request.query_params.get('limit', 100))
        qs = Event.objects.select_related('device').all()
        if metric:
            qs = qs.filter(metric=metric)
        return qs.order_by('-timestamp')[:limit]
