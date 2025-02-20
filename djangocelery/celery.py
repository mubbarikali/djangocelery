import os
from time import sleep
from datetime import timedelta
from celery.schedules import crontab

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelery.settings')

app = Celery('djangocelery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
# @app.task
# def add(x, y):
#     sleep(10)
#     return x+y




# # Without timedelta
# app.conf.beat_schedule = {
#     'session_cleanup': {
#     'task': 'myapp.tasks.clear_session_cache',
#     'schedule': 10,
#     'args': ('777', )
#     }

# }


# # With timedelta
# app.conf.beat_schedule = {
#     'session_cleanup': {
#     'task': 'myapp.tasks.clear_session_cache',
#     'schedule': timedelta(seconds=10),
#     'args': ('777', )
#     }

# }


# With crontab
app.conf.beat_schedule = {
    'session_cleanup': {
    'task': 'myapp.tasks.clear_session_cache',
    'schedule': crontab(minute='*/1'),
    'args': ('777', )
    }

}