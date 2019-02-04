from time import sleep
from celery import Celery

app = Celery(
    'celeryconfig',
    broker='redis://localhost:6379/0',
    backend='db+postgresql://learnpython_user:zxcdsaqwe@localhost/learnpython_db',
)

@app.task
def process(text: str) -> None:
    print('Got task, id: {}'.format(text))
    sleep(0.5)
    print("Okay! Bye!")

@app.task
def reverse(text):
    print(text[::-1])
