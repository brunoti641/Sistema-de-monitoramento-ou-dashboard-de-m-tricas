from django.urls import path
from django.contrib import admin
from monitor.views import IngestView, RecentMetricsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ingest/', IngestView.as_view(), name='ingest'),
    path('api/recent/', RecentMetricsView.as_view(), name='recent-metrics'),
]
