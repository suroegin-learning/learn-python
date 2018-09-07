from time import sleep
from celery import Celery
from selenium.webdriver import Chrome

app = Celery(
    'celeryconfig',
    broker='redis://localhost:6379/0',
    backend='db+postgresql://learnpython_user:zxcdsaqwe@localhost/learnpython_db',
)

browser = Chrome(executable_path="/home/suroegin/Documents/PROJECTS/JOB/PUBLICISGROUP/discoverability3/discoverability/jobs/chromedriver")

@app.task
def open_page_and_return_page_source(url: str) -> int:
    browser.get(url)
    return len(browser.page_source)
