from celery import Celery

app = Celery(
    'tasks-inside-class',
    broker='redis://localhost:6379/1',
    backend='db+postgresql://learnpython_user:zxcdsaqwe@localhost/learnpython_db',
    include=['test.package1.tasks']
)
