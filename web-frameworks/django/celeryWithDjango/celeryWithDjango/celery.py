import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celeryWithDjango.settings")

app = Celery('celeryWithDjango')
app.config_from_object("django.conf:settings")

# Load task modules all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-minute': {
        'task': 'publish.tasks.send_view_count_report',
        'schedule': crontab(),
    },
}