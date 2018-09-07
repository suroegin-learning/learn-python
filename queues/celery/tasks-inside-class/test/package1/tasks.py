from time import sleep

from celery import Celery

app = Celery()
app.config_from_object('test.celery_config')

@app.task
def process(text: str) -> None:
    print('Got task, id: {}'.format(text))
    sleep(0.5)
    print("Okay! Bye!")

@app.task
def reverse(text):
    print(text[::-1])
