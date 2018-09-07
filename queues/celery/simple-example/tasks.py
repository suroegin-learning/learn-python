from time import sleep
from celery.task import task

@task
def fav_doctor():
    print("Pow wow!..")
    sleep(10)
    print("Okay! Bye!")
