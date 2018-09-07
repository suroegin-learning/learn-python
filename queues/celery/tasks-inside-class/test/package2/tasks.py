from time import sleep

from test.celery_config import app

@app.task
def process2(text: str) -> None:
    print('Got task, id: {}'.format(text))
    sleep(0.5)
    print("Okay! Bye!")

@app.task
def reverse2(text):
    print(text[::-1])
