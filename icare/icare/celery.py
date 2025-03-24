import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'icare.settings')

app = Celery('icare')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



app.conf.beat_schedule = {
    'daily_summary': {
        'task': 'core.tasks.daily_summary',
        'schedule': timedelta(seconds=10),
    },
}