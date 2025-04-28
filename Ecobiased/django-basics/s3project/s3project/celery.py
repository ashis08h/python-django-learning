from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 's3project.settings')

# create the celery app
app = Celery('s3project')

# Load the task modules from all registered django apps configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from all installed apps.
app.autodiscover_tasks()

# define the periodic task schedule
app.conf.beat_schedule = {
    'run-every-day': {
        'task': 's3app.tasks.periodic_task',
        'schedule': crontab(hour=0, minute=0) # runs everyday at midnight.
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
