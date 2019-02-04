from celery_config import app
from browsers import chrome_for_google, chrome_for_yandex

jobs = [
    {"search_engine": "google", "url": "https://mail.ru"},
    {"search_engine": "yandex", "url": "https://yandex.ru"},
    {"search_engine": "google", "url": "https://audi.com"},
    {"search_engine": "yandex", "url": "https://psw.ru"},
    {"search_engine": "google", "url": "https://google.com"},
    {"search_engine": "google", "url": "https://my.mail.ru"},
    {"search_engine": "google", "url": "https://ok.ru"},
    {"search_engine": "yandex", "url": "https://youla.ru/"},
    {"search_engine": "yandex", "url": "https://horo.mail.ru/"},
    {"search_engine": "yandex", "url": "https://tv.mail.ru/moskva/"}


]


@app.task(name='fetch_page')
def fetch_page(job):

    if job['search_engine'] == 'google':
        """
        Google
        """
        try:
            chrome_for_google.implicitly_wait(10)
            chrome_for_google.get(job['url'])
        except Exception as exp:
            print(f"EXCEPTION!!! ==> {str(exp)}")
        print(f"[{job['search_engine']} - Site opened: {job['url']}]")
        try:
            return {
                'search_engine': job['search_engine'],
                'url': job['url'],
                'len': len(chrome_for_google.page_source)
            }
        except Exception as exp:
            return {
                'search_engine': job['search_engine'],
                'len': None,
                'url': job['url'],
                'exp': str(exp)
            }

    else:
        """
        Yandex
        """
        try:
            chrome_for_yandex.implicitly_wait(10)
            chrome_for_yandex.get(job['url'])
        except Exception as exp:
            print(f"EXCEPTION!!! ==> {str(exp)}")
        print(f"[{job['search_engine']} - Site opened: {job['url']}]")
        try:
            return {
                'search_engine': job['search_engine'],
                'url': job['url'],
                'len': len(chrome_for_yandex.page_source)
            }
        except Exception as exp:
            return {
                'search_engine': job['search_engine'],
                'len': None,
                'url': job['url'],
                'exp': str(exp)
            }


@app.task(name='print_current_url')
def print_current_url(obj):
    if obj['search_engine'] == 'google':
        if obj['len'] is not None:
            print(obj)
    else:
        print(obj)


@app.task
def do(job):
    # chain = fetch_page.s(job) | print_current_url.s()
    # result = chain()
    # print(type(result))
    # return None
    fetch_page.delay(job)
    return None


@app.task
def gen_tasks():
    for job in jobs:
        do.delay(job)

