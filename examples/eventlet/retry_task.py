
import random
import string
import pydash as _
from pydash.utilities import retry
from datetime import datetime
from celery import task
import requests

@retry(attempts=5, delay=1.0, scale=2.0)
def task_that_retries(name):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Running task [{name}]")
    raise Exception("Error")

@task()
def celery_task():
    task_that_retries(''.join(random.sample(string.digits, 8)))

@task()
def celery_https_task():
    response = requests.get('https://slowwly.herokuapp.com/delay/3000/url/https://api.argyle.io/v1/')
    return response.status_code
