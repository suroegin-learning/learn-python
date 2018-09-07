CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 6379
BROKER_URL = f"redis://{BROKER_HOST}:{BROKER_PORT}/0"

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'doctor-every-10-seconds': {
        'task': 'tasks.fav_doctor',
        'schedule': timedelta(seconds=10),
    }
}
