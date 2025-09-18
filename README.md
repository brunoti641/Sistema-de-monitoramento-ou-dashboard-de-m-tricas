# monitoring_system (skeleton)
Projeto Django + DRF para ingestão de métricas de sensores e integração com InfluxDB (ou TimescaleDB).
Este é um esqueleto para estudo e experimentação local (usa SQLite por padrão para metadados).

Como usar (local):
1. Crie virtualenv (Python 3.11+ recomendado)
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py createsuperuser` (opcional)
5. `python manage.py runserver`

Endpoints principais:
- POST /api/ingest/  (body: {"device_id":"dev1","metric":"temperature","value":23.5,"timestamp":"2025-09-18T22:00:00Z"})
- GET  /api/recent/?metric=temperature&limit=50
