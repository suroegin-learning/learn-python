import sys
from time import sleep

from celery_config import app

sys.path.append('..')


@app.task(name='package1.tasks.process')
def process(text: str) -> None:
    print('Got task, text: {}'.format(text))
    print("Okay! Bye!")


@app.task(name='package1.tasks.reverse')
def reverse(text):
    sleep(2)
    return text[::-1]
