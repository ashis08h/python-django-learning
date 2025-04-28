# command to install celery and redis
# pip install celery
# pip install redis

from celery import shared_task
from time import sleep


@shared_task
def add(x, y):
    sleep(10)
    return (x+y)
