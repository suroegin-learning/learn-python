import os
import sys

from celery import Celery

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Celery(
    'celery_config',
    broker='redis://localhost:6379/4',
    backend='redis://localhost:6379/5',

)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Moscow',
    enable_utc=True
)

app.autodiscover_tasks(
    ['package1', 'package2', 'class_package']
)
